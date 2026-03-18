INF = 1e9

N = int(input())
answer = [INF] * N
answer[0] = 0
checkers = [list(map(int, input().split())) for _ in range(N)]

xs = [x for x, _ in checkers]
ys = [y for _, y in checkers]

for x in xs:
    for y in ys:
        move = []
        for cx, cy in checkers:
            move.append(abs(x - cx) + abs(y - cy))
        move.sort()
        for i in range(N):
            if answer[i] > sum(move[: i + 1]):
                answer[i] = sum(move[: i + 1])
print(*answer)
