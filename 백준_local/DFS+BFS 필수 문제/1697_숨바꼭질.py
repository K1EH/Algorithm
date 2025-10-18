from collections import deque

INF = 100_001
N, K = map(int, input().split())

start = (N, 0)

visited = [False] * INF

queue = deque([start])

visited.append(N)
while queue:
    pos, move = queue.popleft()
    if pos == K:
        print(move)
        break
    steps = (pos - 1, pos + 1, pos * 2)
    for step in steps:
        if 0<= step <= INF and not visited[step]:
            visited[step] = True
            queue.append((step, move + 1))
