N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr, res = [], []


def rec(n):
    if n == M:
        res.append(" ".join(map(str, arr)))
        return
    for i in nums:
        arr.append(i)
        rec(n + 1)
        arr.pop()


rec(0)
print("\n".join(res))
