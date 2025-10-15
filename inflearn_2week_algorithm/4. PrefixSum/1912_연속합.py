INF = 1e9
N = int(input())
nums = list(map(int, input().split()))
prefix_sum = [-INF] * (N + 1)

for i in range(N):
    prefix_sum[i + 1] = max(prefix_sum[i] + nums[i], nums[i])
print(max(prefix_sum))