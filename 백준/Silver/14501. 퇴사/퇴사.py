N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]

ans = 0


def recursion(idx, money):
    global ans
    if idx == N:
        if ans < money:
            ans = money
        return
    duration, profit = schedule[idx]
    if idx + duration <= N:
        recursion(idx + duration, money + profit)
    recursion(idx + 1, money)


recursion(0, 0)
print(ans)
