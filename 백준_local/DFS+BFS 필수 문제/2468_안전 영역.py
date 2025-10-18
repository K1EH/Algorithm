from collections import deque


def bfs(graph, start, visited, height):
    queue = deque([start])
    y, x = start
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        for direction in directions:
            dy, dx = direction
            ny, nx = y + dy, x + dx
            if (
                (0 <= ny < N and 0 <= nx < N)
                and not visited[ny][nx]
                and graph[ny][nx] > height
            ):
                queue.append((ny, nx))
                visited[ny][nx] = True


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
heights = {0} # 비가 오지 않은 경우도 계산
directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
ans = []

for y in range(N):
    for x in range(N):
        heights.add(graph[y][x])

for height in heights:
    visited = [[False] * N for _ in range(N)]
    count = 0
    for y in range(N):
        for x in range(N):
            if not visited[y][x] and graph[y][x] > height:
                bfs(graph, (y, x), visited, height)
                count += 1
    ans.append(count)
print(max(ans))
