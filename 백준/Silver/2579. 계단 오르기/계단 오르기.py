N = int(input())
stairs = list(int(input()) for _ in range(N))
dp = [0] * N

for i in range(N):
    if i == 0:
        dp[i] = stairs[i]
    elif i == 1:
        dp[i] = stairs[i] + stairs[i - 1]
    elif i == 2:
        dp[i] = stairs[i] + max(stairs[i - 1], stairs[i - 2])
    else:
        dp[i] = stairs[i] + max(stairs[i - 1] + dp[i - 3], dp[i - 2])
print(dp[N - 1])
