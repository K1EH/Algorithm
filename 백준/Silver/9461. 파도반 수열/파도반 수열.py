T = int(input())

dp = [-1] * 101
dp[1:4] = 1, 1, 1
for _ in range(T):
    N = int(input())
    for i in range(3, N + 1):
        if dp[i] != -1:
            continue
        dp[i] = dp[i - 2] + dp[i - 3]
    print(dp[N])