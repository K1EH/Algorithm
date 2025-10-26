N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

arr, res = [], []


def rec(number):
    if number == M:
        res.append(" ".join(map(str, arr)))
        return
    for i in nums:
        if i not in arr and i > arr[-1] if arr else True:
            arr.append(i)
            rec(number + 1)
            arr.pop()


rec(0)
print("\n".join(res))
