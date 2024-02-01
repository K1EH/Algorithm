N = int(input())
for _ in range(N):
    K = int(input())
    dp = [0] * (K + 1)
    for i in range(1, K + 1):
        if i <= 3:
            dp[i] = 2 ** (i - 1)
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[i])