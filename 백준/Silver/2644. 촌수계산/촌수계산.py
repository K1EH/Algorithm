from collections import defaultdict, deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 0
    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if visited[next] == -1:
                queue.append(next)
                visited[next] = visited[node] + 1


N = int(input())
start, end = map(int, input().split())
M = int(input())

graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [-1] * (N + 1)

bfs(graph, start, visited)
print(visited[end])
