N = int(input())
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    count = 1
    while queue:
        node = queue.popleft()
        y, x = node
        for direction in directions:
            dy, dx = direction
            ny, nx = y + dy, x + dx
            if (
                (0 <= ny < N and 0 <= nx < N)
                and graph[ny][nx] == 1
                and not visited[ny][nx]
            ):
                queue.append((ny, nx))
                visited[ny][nx] = True
                count += 1
    return count


ans = []
for y in range(N):
    for x in range(N):
        if grid[y][x] == 1 and not visited[y][x]:
            ans.append(bfs(grid, (y, x), visited))
ans.sort()
print(len(ans))
for a in ans:
    print(a)
