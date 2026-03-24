answer = 1e9
N = int(input())
ingredient = [list(map(int, input().split())) for _ in range(N)]


def recursion(idx, S, B, used):
    global answer
    if idx == N:
        if used:
            answer = min(answer, abs(S - B))
        return
    recursion(idx + 1, S * ingredient[idx][0], B + ingredient[idx][1], used + 1)
    recursion(idx + 1, S, B, used)


recursion(0, 1, 0, 0)
print(answer)
