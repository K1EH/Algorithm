N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
pos = [list(map(int, input().split())) for _ in range(M)]

prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]
for x in range(1, N + 1):
    for y in range(1, N + 1):
        prefix_sum[x][y] = (
            grid[x - 1][y - 1]
            + prefix_sum[x - 1][y]
            + prefix_sum[x][y - 1]
            - prefix_sum[x - 1][y - 1]
        )
for p in pos:
    x1, y1, x2, y2 = p
    print(
        prefix_sum[x2][y2]
        - prefix_sum[x1 - 1][y2]
        - prefix_sum[x2][y1 - 1]
        + prefix_sum[x1 - 1][y1 - 1]
    )
