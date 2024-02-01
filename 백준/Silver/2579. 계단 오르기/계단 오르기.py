N = int(input())
stairs = [0] * (N + 1)
for i in range(1, N + 1):
    stairs[i] = int(input())
dp = [0] * (N + 1)
if N <= 2:
    print(sum(stairs))
else:
    for i in range(1, N + 1):
        dp[i] = stairs[i] + max(stairs[i - 1] + dp[i - 3], dp[i - 2])
    print(dp[N])