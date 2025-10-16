from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[0][0] = True
    while queue:
        node = queue.popleft()
        y, x = node
        for direction in directions:
            dy, dx = direction
            ny, nx = y + dy, x + dx
            # print(f"current{y, x}")
            if (0 <= ny < N and 0 <= nx < M) and not visited[ny][nx] and graph[ny][nx]:
                # print(f"visit!{ny, nx}")
                graph[ny][nx] += graph[y][x]
                queue.append([ny, nx])
                visited[ny][nx] = True
            # else:
            #     print(f"can not visit!{ny, nx}")


N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
start = [0, 0]

bfs(maze, start, visited)
print(maze[N - 1][M - 1])
