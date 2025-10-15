N, K = map(int, input().split())
temperature = list(map(int, input().split()))
prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + temperature[i]

max_t = -(10**9)

for i in range((N + 1) - K):
    max_t = max(max_t, prefix_sum[i + K] - prefix_sum[i])

print(max_t)
