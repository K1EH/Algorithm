N, M = map(int, input().split())

visited = [False] * (N + 1)
arr = []


def recursion():
    if len(arr) == M:
        print(*arr)
        return
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)

            recursion()

            visited[i] = False
            arr.pop()


recursion()
