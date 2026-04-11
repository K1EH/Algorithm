N = int(input())
dp = [[0] * 10 for _ in range(N)]
dp[0] = [0] + [1] * 9
for i in range(1, N):
    for k in range(10):
        if k == 0:
            dp[i][k] = dp[i - 1][1]
        elif k == 9:
            dp[i][k] = dp[i - 1][8]
        else:
            dp[i][k] = dp[i - 1][k - 1] + dp[i - 1][k + 1]
print(sum(dp[N - 1]) % 1_000_000_000)
