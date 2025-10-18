from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [False] * (F + 1)

queue = deque([(S, 0)])
while queue:
    level, move = queue.popleft()
    if level == G:
        print(move)
        break
    nexts = [level + U, level - D]
    for next in nexts:
        if 1 <= next <= F and not visited[next]:
            queue.append((next, move + 1))
            visited[next] = True
else:
    print("use the stairs")
