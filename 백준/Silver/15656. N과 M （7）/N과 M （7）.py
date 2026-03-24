N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = []


def recursion():
    if len(arr) == M:
        print(*arr)
        return
    for i in range(N):
        arr.append(nums[i])
        recursion()
        arr.pop()


recursion()
