N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def rec(idx, profit):
    global ans
    if idx == N:
        if ans < profit:
            ans = profit
        return
    t, p = table[idx]
    if idx + t <= N:
        rec(idx + t, profit + p)
    rec(idx + 1, profit)


rec(0, 0)
print(ans)
