N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
ans = dlsvm0


def rec(idx, weight, value):
    global ans
    if idx == N:
        ans = max(ans, value)
        return
    w, v = items[idx]
    if weight + w <= K:
        rec(idx + 1, weight + w, value + v)
    rec(idx + 1, weight, value)


rec(0, 0, 0)
print(ans)
