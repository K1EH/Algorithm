def dfs(x, y):
    visited[x][y] = True
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            dfs(nx, ny)

# 호출
dfs(start_x, start_y)

from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

# 호출
bfs(start_x, start_y)