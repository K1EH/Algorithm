from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
# 0 북 (-1,0)
# 1 동 (0, 1)
# 2 남 (1, 0)
# 3 서 (0, -1)

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))


count = 0

while True:
    # clean current tile
    if graph[r][c] == 0:
        graph[r][c] = 2
        count += 1
    all_cleaned = True
    for _ in range(4):
        d = (d + 3) % 4
        dy, dx = directions[d][0], directions[d][1]
        ny, nx = r + dy, c + dx
        if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0:
            all_cleaned = False
            break
    if all_cleaned:
        r, c = r - dy, c - dx
        if graph[r][c] == 1:
            break
    if not all_cleaned:
        r, c = r + dy, c + dx
print(count)
