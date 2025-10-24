N, M = map(int, input().split())


def recursion(number):
    if number == M:
        result.append(" ".join(map(str, arr)))
        return
    for i in range(1, N + 1):
        arr.append(i)
        recursion(number + 1)
        arr.pop()


arr = []
result = []
recursion(0)
print("\n".join(result))
