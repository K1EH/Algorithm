N = int(input())
grid = []

for _ in range(N):
    grid.append(input())

visited = [[False] * N for _ in range(N)]

direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def dfs(y, x):
    visited[y][x] = True
    count = 1
    for dy, dx in direction:
        ny = y + dy
        nx = x + dx
        if (0 <= ny < N and 0 <= nx < N) and not visited[ny][nx] and grid[ny][nx] == '1':
                count += dfs(ny, nx)
    return count
res = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == '1' and not visited[i][j]:
            res.append(dfs(i, j))
res.sort()
print(len(res))
for i in res:
     print(i)