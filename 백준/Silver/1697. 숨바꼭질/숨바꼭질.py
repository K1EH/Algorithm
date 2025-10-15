from collections import deque
N, K = map(int, input().split())

visited = [False] * 100001
def bfs (N, K, visited):
    visited[N] = True
    time = 0
    queue = deque([[N, time]])

    while queue:
        pos, time = queue.popleft()
        if pos == K:
            print(time)
            break
        nexts = [pos - 1, pos + 1, pos * 2]
        for next in nexts:
            if 0 <= next < 100001 and not visited[next]:
                visited[next] = True
                queue.append([next, time + 1])

bfs(N, K , visited)