INF = 1e10
N = int(input())
ingredient = [list(map(int, input().split())) for _ in range(N)]


flavor = INF


def rec(idx, sour, bitter, used):
    global flavor
    if idx == N:
        if used:
            flavor = min(flavor, abs(sour - bitter))
        return
    rec(idx + 1, sour * ingredient[idx][0], bitter + ingredient[idx][1], True)
    rec(idx + 1, sour, bitter, used)


rec(0, 1, 0, False)

print(flavor)
