from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
is_one = True

year = 0
while is_one:
    queue = deque()
    water = [[0] * M for _ in range(N)]

    for y in range(N):
        for x in range(M):
            if graph[y][x] > 0:
                queue.append((y, x))

    if not queue:
        print(0)
        break

    while queue:
        y, x = queue.popleft()
        for direction in directions:
            dy, dx = direction
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0:
                water[y][x] += 1
        if water[y][x] == 4:
            is_one = False
            print(year)
            break
    for y in range(N):
        for x in range(M):
            if graph[y][x] > 0:
                # Updating graph
                graph[y][x] = max(graph[y][x] - water[y][x], 0)
    year += 1
