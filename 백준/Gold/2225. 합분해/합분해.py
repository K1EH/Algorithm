N, K = map(int, input().split())
dp = [[1] * (N + 1) for _ in range(K + 1)]
nums = [i for i in range(0, N + 1)]
for i in range(2, K + 1):
    for j in range(1, N + 1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000

print(dp[K][N])
