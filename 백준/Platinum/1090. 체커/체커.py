def cal_dist(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return abs(x1 - x2) + abs(y1 - y2)

N = int(input())

INF = 1e9
ans = [INF] * N
ans[0] = 0

coordinates = [list(map(int, input().split())) for _ in range(N)]
xs, ys = [], []
for coordinate in coordinates:
    xs.append(coordinate[0])
    ys.append(coordinate[1])

for x in xs:
    for y in ys:
        dist = []
        for coordinate in coordinates:
            dist.append(cal_dist([x, y], coordinate))
        dist.sort()
        for i in range(1, len(dist)):
            dist[i] = dist[i - 1] + dist[i]
            if dist[i] < ans[i]:
                ans[i] = dist[i]

print(*ans)
