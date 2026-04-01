N = int(input())
arr = list(map(int, input().split()))
prefix_sum = [-1e4] * (N + 1)

for i in range(N):
    prefix_sum[i + 1] = max(arr[i], arr[i] + prefix_sum[i])
print(max(prefix_sum))
