N, M = map(int, input().split())
arr = []


def recursion(n):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(n, N + 1):
        arr.append(i)
        recursion(i)
        arr.pop()


recursion(1)
