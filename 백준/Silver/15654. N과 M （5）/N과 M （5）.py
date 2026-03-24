N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

visited = [False] * N
arr = []


def recursion():
    if len(arr) == M:
        print(*arr)
        return
    for i, v in enumerate(nums):
        if not visited[i]:
            visited[i] = True
            arr.append(v)
            recursion()
            arr.pop()
            visited[i] = False
recursion()
