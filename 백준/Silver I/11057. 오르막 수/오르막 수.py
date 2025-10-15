N = int(input())
dp = [[1] * (10) for _ in range(N)]

for x in range(1, N):
    for y in range(10):
        if y == 0:
            dp[x][y] = (sum(dp[x-1])) % 10007
        else:
            dp[x][y] = (dp[x][y-1] - dp[x-1][y-1]) % 10007
print(sum(dp[N-1]) % 10007)