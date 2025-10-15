N = int(input())

RGB = [[0, 0, 0]]

for _ in range(N):
    RGB.append(list(map(int, input().split())))
#print(RGB)

DP = [0] * (N + 1)
DP[1] = min(RGB[1])
#print(DP)

for i in range(2, N + 1):
    RGB[i][0] += min(RGB[i-1][1], RGB[i-1][2])
    RGB[i][1] += min(RGB[i-1][0], RGB[i-1][2])
    RGB[i][2] += min(RGB[i-1][0], RGB[i-1][1])

    DP[i] = min(RGB[i][0], RGB[i][1], RGB[i][2])
print(DP[N])