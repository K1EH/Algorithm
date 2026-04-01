N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (N + 1) for _ in range(N + 1)]


for y in range(N):
    for x in range(y + 1):
        if x == 0:
            dp[y + 1][x + 1] = arr[y][x] + dp[y][x + 1]
        if x == y:
            dp[y + 1][x + 1] = arr[y][x] + dp[y][x]
        else:
            dp[y + 1][x + 1] = arr[y][x] + max(dp[y][x + 1], dp[y][x])

print(max(dp[N]))
