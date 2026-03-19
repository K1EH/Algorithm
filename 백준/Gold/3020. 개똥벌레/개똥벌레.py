import sys

input = sys.stdin.readline

INF = 1e9
N, H = map(int, input().split())
columns = []
ans, count = INF, 0

for _ in range(N):
    columns.append(int(input()))
imos = list(0 for _ in range(H))

for i in range(N):

    if i % 2 == 0:  # even
        imos[0] += 1
        imos[columns[i]] -= 1
    else:  # odd
        imos[H - columns[i]] += 1

prefix = [0 for _ in range(H + 1)]

for i in range(H):
    prefix[i + 1] = prefix[i] + imos[i]
    if ans > prefix[i + 1]:
        ans = prefix[i + 1]
        count = 1
    elif ans == prefix[i + 1]:
        count += 1
print(ans, count)
