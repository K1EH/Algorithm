N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()


def recursion(number):
    if number == M:
        result.append(" ".join(map(str, arr)))
    for n in nums:
        if n not in arr:
            arr.append(n)
            recursion(number + 1)
            arr.pop()


arr, result = [], []
recursion(0)
print("\n".join(result))
