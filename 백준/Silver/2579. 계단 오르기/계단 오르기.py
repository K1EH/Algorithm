N = int(input())
stairs = list(int(input()) for _ in range(N))
dp = [-1] * N


for i in range(N):
    if i == 0:
        dp[0] = stairs[0]
    elif i == 1:
        dp[i] = stairs[i] + dp[0]
    elif i == 2:
        dp[i] = stairs[i] + max(stairs[0], stairs[1])
    else:
        dp[i] = stairs[i] + max(stairs[i - 1] + dp[i - 3], dp[i - 2])

print(dp[N - 1])
