import sys

input = sys.stdin.readline

obs, count = 1e9, 1

N, H = map(int, input().split())

arr = [0] * H
prefix = [0] * (H + 1)

for i in range(N):
    length = int(input())
    if i % 2 == 0:
        arr[0] += 1
        arr[length] -= 1
    else:
        arr[H - length] += 1

for i in range(H):
    p = prefix[i] + arr[i]
    prefix[i + 1] = p
    if p < obs:
        obs = p
        count = 1
    elif p == obs:
        count += 1

print(obs, count)
