from collections import defaultdict


def dfs(graph, node, visited):
    visited[node] = 1

    for next in graph[node]:
        if not visited[next]:
            dfs(graph, next, visited)


N = int(input())
M = int(input())

graph = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)
dfs(graph, 1, visited)
print(sum(visited) - 1)
