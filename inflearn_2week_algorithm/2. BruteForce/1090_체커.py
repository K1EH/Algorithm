def cal_dist(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return abs(x1 - x2) + abs(y1 - y2)


N = int(input())
checkers = [list(map(int, input().split())) for _ in range(N)]
INF = 10**9
ans = [INF] * N
ans[0] = 0

xs = [x for x, _ in checkers]
ys = [y for _, y in checkers]


# for all of candidate coordinates
for x in xs:
    for y in ys:
        # calculating distance to checkers
        dist = []
        for checker in checkers:
            dist.append(cal_dist((x, y), checker))
        dist.sort()
        # calculating prefix-sum
        for i in range(1, len(dist)):
            dist[i] = dist[i - 1] + dist[i]
            ans[i] = min(dist[i], ans[i])
print(*ans)
