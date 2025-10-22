from collections import deque, defaultdict

T = int(input())
LIMIT = 1000


def movable(p1, p2):
    if (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])) <= LIMIT:
        return True
    else:
        return False


for _ in range(T):
    N = int(input())
    home = tuple(map(int, input().split()))
    stores = [tuple(map(int, input().split())) for _ in range(N)]
    festival = tuple(map(int, input().split()))

    stores.append(home)
    stores.append(festival)

    graph = defaultdict(list)
    for i in range(len(stores)):
        for j in range(len(stores)):
            if movable(stores[i], stores[j]):
                graph[stores[i]].append(stores[j])

    queue = deque([home])
    visited = {home}
    while queue:
        node = queue.popleft()
        if node == festival:
            print("happy")
            break
        for next in graph[node]:
            if next not in visited:
                queue.append(next)
                visited.add(next)
    else:
        print("sad")
