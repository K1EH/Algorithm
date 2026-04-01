N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N)]

dp[0] = arr[0].copy()

for i in range(1, N):
    for color in range(3):
        dp[i][color] = arr[i][color] + min(dp[i - 1][color - 1], dp[i - 1][color - 2])
print(min(dp[N - 1]))
