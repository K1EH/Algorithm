from collections import deque


def bfs(graph, start, visited):
    y, x = start
    queue = deque([(y, x)])
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (
                (0 <= ny < N and 0 <= nx < M)
                and graph[ny][nx] > 0
                and not visited[ny][nx]
            ):
                queue.append((ny, nx))
                visited[ny][nx] = True


# Input
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
directions = ((1, 0), (-1, 0), (0, -1), (0, 1))

year = 0

ice_pos = []
# list up current position of iceberg
for y in range(1, N - 1):
    for x in range(1, M - 1):
        if graph[y][x] > 0:
            # y, x, water
            ice_pos.append([y, x])

# At each year
while True:
    count = 0
    info = []
    for p in ice_pos:
        info.append([p[0], p[1], 0])

    # counting the number of seas near by iceberg
    for i in range(len(info)):
        y, x = info[i][0], info[i][1]
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (0 <= ny < N and 0 <= nx < M) and graph[ny][nx] == 0:
                info[i][2] += 1
    # updating height of ice
    ice_pos = []
    for i in range(len(info)):
        y, x = info[i][0], info[i][1]
        graph[y][x] = max(0, graph[y][x] - info[i][2])
        if graph[y][x] > 0:
            ice_pos.append([y, x])

    # bfs검사
    visited = [[False] * M for _ in range(N)]
    for y, x in ice_pos:
        if graph[y][x] > 0 and not visited[y][x]:
            bfs(graph, (y, x), visited)
            count += 1
    year += 1

    if count == 0:
        print(0)
        break
    elif count >= 2:
        print(year)
        break
