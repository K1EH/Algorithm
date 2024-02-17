T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7]
    if N >= 10:
        for i in range(10, N + 1):
            dp.append(dp[i - 1]+ dp[i - 5])
    print(dp[N])