INF = 1e9
N = int(input())
answer = [INF] * N
answer[0] = 0

checkers = [list(map(int, input().split())) for _ in range(N)]
xs = [x for x, y in checkers]
ys = [y for x, y in checkers]
for x in xs:
    for y in ys:
        move = []
        for checker in checkers:
            dx, dy = checker
            move.append(abs(x - dx) + abs(y - dy))
        move.sort()

        for i in range(1, N):
            candidate = sum(move[: i + 1])
            if answer[i] > candidate:
                answer[i] = candidate
print(*answer)
