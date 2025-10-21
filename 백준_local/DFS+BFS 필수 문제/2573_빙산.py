from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
year = 0

while True:
    ice = {}
    for y in range(N):
        for x in range(M):
            if graph[y][x] > 0:
                ice[(y, x)] = 0

    for key in ice.keys():
        y, x = key
        for direction in directions:
            dy, dx = direction
            ny, nx = y + dy, x + dx
            if (0 <= ny < N and 0 <= nx < M) and graph[ny][nx] == 0:
                ice[(y, x)] += 1

    for key in ice.keys():
        y, x = key
        graph[y][x] = max(0, graph[y][x] - ice[(y, x)])
        ice[(y, x)] = False

    remaining = [(y, x) for (y, x) in ice.keys() if graph[y][x] > 0]
    if not remaining:
        print(0)
        break
    count = 0
    for key in ice.keys():
        y, x = key
        if graph[y][x] > 0 and not ice[key]:
            queue = deque([key])
            ice[key] = True
            while queue:
                y, x = queue.popleft()
                for direction in directions:
                    dy, dx = direction
                    ny, nx = y + dy, x + dx
                    if (
                        (0 <= ny < N and 0 <= nx < M)
                        and graph[ny][nx] > 0
                        and not ice[(ny, nx)]
                    ):
                        queue.append((ny, nx))
                        ice[(ny, nx)] = True
            count += 1
    year += 1
    if count != 1:
        print(year)
        break
