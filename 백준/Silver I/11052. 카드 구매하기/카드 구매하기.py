N = int(input())
temp = list(map(int, input().split()))
P = [0]
DP = [0] * (N + 1)
# P[1] ~, DP[1]~ 로 초기화
for i in range(len(temp)):
    P.append(temp[i])
    DP[i + 1] = temp[i]

# DP[i] = max(DP[i], DP[i-1] + P[1] ...)
for i in range(1, N + 1):
    temp = [DP[i]]
    for k in range(1, i):
        temp.append(DP[i - k] + P[k])
    DP[i] = max(temp)
print(DP[N])