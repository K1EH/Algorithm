import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

distance = [INF] * (V + 1)
graph = [[] for _ in range(V + 1)]
for _ in range(1, E + 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)
for i in distance[1::]:
    if i == INF:
        print("INF")
    else:
        print(i)