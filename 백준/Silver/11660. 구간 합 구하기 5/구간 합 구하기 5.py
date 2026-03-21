N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
coordinates = [list(map(int, input().split())) for _ in range(M)]
prefix = [[0] * (N + 1) for _ in range(N + 1)]

for y in range(N):
    for x in range(N):
        prefix[y + 1][x + 1] = (
            arr[y][x] + prefix[y][x + 1] + prefix[y + 1][x] - prefix[y][x]
        )
for y1, x1, y2, x2 in coordinates:
    ans = (
        prefix[y2][x2]
        - prefix[y2][x1 - 1]
        - prefix[y1 - 1][x2]
        + prefix[y1 - 1][x1 - 1]
    )
    print(ans)
