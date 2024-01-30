from collections import deque
T = int(input())

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def bfs(x, y, visited):
    count = 1
    queue = deque([[x, y, 1]])
    visited[y][x] = True
    while queue:
        x, y, count = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and grid[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append([nx, ny, count + 1])
    return count

for _ in range(T):
    M, N, K = map(int, input().split())

    visited = [[False] * M for _ in range(N)]
    grid = [[False] * M for _ in range(N)]
    res = []
    count = 0

    for _ in range(K):
        x, y = map(int, input().split())
        grid[y][x] = True
    for i in range(M):
        for j in range(N):
            if grid[j][i] and not visited[j][i]:
                res.append(bfs(i, j, visited))
            
    print(len(res))