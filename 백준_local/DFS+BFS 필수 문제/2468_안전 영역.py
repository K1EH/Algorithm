from collections import deque


def bfs(grid, start, visited):
    y, x = start
    queue = deque([(y, x)])
    visited[(y, x)] = True
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (
                (0 <= ny < N and 0 <= nx < M)
                and grid[ny][nx] > 0
                and not visited[(ny, nx)]
            ):
                queue.append((ny, nx))
                visited[(ny, nx)] = True


# Input
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

ice_pos = []
directions = ((1, 0), (-1, 0), (0, -1), (0, 1))

for y in range(N):
    for x in range(M):
        if grid[y][x] > 0:
            ice_pos.append((y, x))

year = 0
# At each year
while True:
    ice = {}
    visited = {}
    count = 0
    # list up current position of iceberg
    for y, x in ice_pos:
        if grid[y][x] > 0:
            ice[(y, x)] = 0
            visited[(y, x)] = False
    # counting the number of seas near by iceberg
    for y, x in ice.keys():
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if (0 <= ny < N and 0 <= nx < M) and grid[ny][nx] == 0:
                ice[(y, x)] += 1
    # updating height of ice
    for y, x in ice.keys():
        grid[y][x] = max(0, grid[y][x] - ice[(y, x)])

    # bfs검사
    for y, x in ice.keys():
        if grid[y][x] > 0 and not visited[(y, x)]:
            bfs(grid, (y, x), visited)
            count += 1
    year += 1

    if count == 0:
        print(0)
        break
    elif count >= 2:
        print(year)
        break
