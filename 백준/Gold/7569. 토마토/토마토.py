from collections import deque

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

directions = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
queue = deque()

for h in range(H):
    for y in range(N):
        for x in range(M):
            if graph[h][y][x] == 1:
                queue.append((h, y, x))

while queue:
    h, y, x = queue.popleft()
    for dh, dy, dx in directions:
        nh, ny, nx = h + dh, y + dy, x + dx
        if 0 <= nh < H and 0 <= ny < N and 0 <= nx < M and graph[nh][ny][nx] == 0:
            graph[nh][ny][nx] = graph[h][y][x] + 1
            queue.append((nh, ny, nx))

ans = 0
for layer in graph:
    for row in layer:
        if 0 in row:
            print(-1)
            exit(0)
        ans = max(ans, max(row))
print(ans - 1)