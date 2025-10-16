from collections import defaultdict, deque


def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=" ")
    for next in graph[node]:
        if not visited[next]:
            dfs(graph, next, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for next in graph[node]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True


N, M, V = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for key in graph:
    graph[key].sort()

visited = [False] * (N + 1)
dfs(graph, V, visited)
print()
visited = [False] * (N + 1)
bfs(graph, V, visited)
