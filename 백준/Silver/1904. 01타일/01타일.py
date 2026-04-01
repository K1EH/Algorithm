N = int(input())
dp = [0] * (N + 1)
for i in range(N + 1):
    if i in [0, 1, 2, 3]:
        dp[i] = i
    else:
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
print(dp[N])
