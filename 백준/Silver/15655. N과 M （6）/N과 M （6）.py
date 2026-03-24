N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = []


def recursion(idx):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(idx, N):
        arr.append(nums[i])
        recursion(i + 1)
        arr.pop()


recursion(0)
