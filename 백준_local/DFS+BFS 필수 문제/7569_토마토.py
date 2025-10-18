from collections import deque

X, Y, H = map(int, input().split())
graph = []
for h in range(H):
    xy = []
    for y in range(Y):
        xy.append(list(map(int, input().split())))
    graph.append(xy)

directions = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
visited = [[[False] * X for _ in range(Y)] for _ in range(H)]
already_riped = True
cannot_riped = False
ans = 0

queue = deque()
for h in range(H):
    for y in range(Y):
        for x in range(X):
            if graph[h][y][x] == 0:
                already_riped = False
            if graph[h][y][x] == 1:
                queue.append((h, y, x))
                visited[h][y][x] = True
while queue:
    node = queue.popleft()
    h, y, x = node
    for direction in directions:
        dh, dy, dx = direction
        nh, ny, nx = h + dh, y + dy, x + dx
        if 0 <= nh < H and 0 <= ny < Y and 0 <= nx < X:
            if not visited[nh][ny][nx]:
                if graph[nh][ny][nx] == 0:
                    queue.append((nh, ny, nx))
                    visited[nh][ny][nx] = True
                    graph[nh][ny][nx] = graph[h][y][x] + 1

for xy in graph:
    for x in xy:
        if 0 in x:
            cannot_riped = True
        if ans < max(x):
            ans = max(x)

if already_riped:
    print(0)
elif cannot_riped:
    print(-1)
else:
    print(ans - 1)
