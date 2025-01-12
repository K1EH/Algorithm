import sys
import heapq

N = int(sys.stdin.readline())
INF = 1e9
checkers = [list(map(int, input().split())) for _ in range(N)]

checker_x = sorted([checkers[i][0] for i in range(N)])
checker_y = sorted([checkers[i][1] for i in range(N)])


answer = [INF] * N
# 체커 하나가 모이는 경우는 이동 X
answer[0] = 0
# 보드 수를 최소화
for x in checker_x:
    for y in checker_y:
        # x, y 칸까지 각 기물의 이동 횟수
        move = []
        # 체커의 이동 거리는 abs(x - dx) + abs(y - dy)
        for dx, dy in checkers:
            count = abs(x - dx) + abs(y - dy)
            heapq.heappush(move, count)
        # 정렬된 move 배열에서 최소 k개 기물이 모이는 이동 거리의 합은 sum(move[: k + 1])
        pop = 0
        for i in range(N):
            pop += heapq.heappop(move)
            if answer[i] > pop:
                answer[i] = pop
print(*answer)
