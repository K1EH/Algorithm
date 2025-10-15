import sys

input = sys.stdin.readline
INF = 1e9

N, H = map(int, input().split())
obj = list(int(input()) for _ in range(N))

prefix_sum = [0] * (H + 1)

for i in range(N):
    length = obj[i]
    # 석순
    if i % 2 == 0:
        prefix_sum[1] += 1
        prefix_sum[1 + length] -= 1
    # 종유순
    else:
        prefix_sum[-length] += 1

min_obj, count = INF, 0
for i in range(1, H + 1):
    prefix_sum[i] += prefix_sum[i - 1]
    if prefix_sum[i] < min_obj:
        min_obj = prefix_sum[i]
        count = 1
    elif prefix_sum[i] == min_obj:
        count += 1
print(min_obj, count)
