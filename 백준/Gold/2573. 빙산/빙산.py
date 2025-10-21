from collections import deque


def bfs(grid, start, visited):
    y, x = start
    queue = deque([(y, x)])
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (
                (0 <= ny < N and 0 <= nx < M)
                and grid[ny][nx] > 0
                and not visited[ny][nx]
            ):
                queue.append((ny, nx))
                visited[ny][nx] = True


# Input
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
directions = ((1, 0), (-1, 0), (0, -1), (0, 1))

year = 0

candidates = []
# list up current position of iceberg
for y in range(1, N - 1):
    for x in range(1, M - 1):
        if grid[y][x] > 0:
            # y, x, water
            candidates.append([y, x])

# At each year
while True:
    count = 0
    ice = []
    for c in candidates:
        ice.append([c[0], c[1], 0])

    # counting the number of seas near by iceberg
    for i in range(len(ice)):
        y, x = ice[i][0], ice[i][1]
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (0 <= ny < N and 0 <= nx < M) and grid[ny][nx] == 0:
                ice[i][2] += 1
    # updating height of ice
    candidates = []
    for i in range(len(ice)):
        y, x = ice[i][0], ice[i][1]
        grid[y][x] = max(0, grid[y][x] - ice[i][2])
        if grid[y][x] > 0:
            candidates.append([y, x])

    # bfs검사
    visited = [[False] * M for _ in range(N)]
    for i in range(len(ice)):
        y, x = ice[i][0], ice[i][1]
        if grid[y][x] > 0 and not visited[y][x]:
            bfs(grid, (y, x), visited)
            count += 1
    year += 1

    if count == 0:
        print(0)
        break
    elif count >= 2:
        print(year)
        break
