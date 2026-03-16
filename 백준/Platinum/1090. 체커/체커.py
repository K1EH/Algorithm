INF = 1e9

N = int(input())
checkers = [list(map(int, input().split())) for _ in range(N)]

answer = [INF] * N
answer[0] = 0

for dx, _ in checkers:
    for _, dy in checkers:
        move = []
        for x, y in checkers:
            move.append(abs(x - dx) + abs(y - dy))
        move.sort()
        for i in range(N):
            if answer[i] > sum(move[: i + 1]):
                answer[i] = sum(move[: i + 1])
print(*answer)
