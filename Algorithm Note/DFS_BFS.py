# 그래프 정의 (양방향)
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E", "F"],
    "D": ["B"],
    "E": ["C", "G"],
    "F": ["C"],
    "G": ["E"],
}


def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")
    for next in graph[node]:
        if next not in visited:
            dfs(graph, next, visited)


visited = set()
dfs(graph, "A", visited)

from collections import deque

print()


def bfs(graph, start, visited):
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for next in graph[node]:
            if next not in visited:
                queue.append(next)
                visited.add(next)


visited = set()
bfs(graph, "A", visited)
