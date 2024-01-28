N = int(input())

grid = []
for _ in range(N):
    grid.append(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * N for _ in range(N)]

def DFS(x, y):
    global count
    visited[x][y] = True
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<= ny < N and not visited[nx][ny] and grid[nx][ny] == '1':
            DFS(nx, ny)

result = []
for x in range(N):
    for y in range(N):
        if grid[x][y] == '1' and not visited[x][y]:
            count = 0
            DFS(x, y)
            result.append(count)
print(len(result))
for i in sorted(result):
    print(i)
