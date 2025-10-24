N = int(input())
mp, mf, ms, mv = map(int, input().split())
ingredient = [list(map(int, input().split())) for _ in range(N)]
arr = []
ans = []
cost = N * 500 + 1


def rec(idx, p, f, s, v, c):
    global cost, ans
    if idx == N:
        if mp <= p and mf <= f and ms <= s and mv <= v:
            if c < cost or (c == cost and (arr == [] or ans > arr)):
                cost = c
                ans = arr[:]
        return
    np, nf, ns, nv, nc = ingredient[idx]
    arr.append(idx + 1)
    rec(idx + 1, p + np, f + nf, s + ns, v + nv, c + nc)
    arr.pop()
    rec(idx + 1, p, f, s, v, c)


rec(0, 0, 0, 0, 0, 0)
if ans:
    print(cost)
    print(*ans)
else:
    print(-1)
