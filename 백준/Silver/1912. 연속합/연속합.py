n = int(input())
nums = list(map(int, input().split()))

prefix_sum = [0 for _ in range(n + 1)]

count = 0
for i in range(n):
    if (nums[i] + prefix_sum[i]) < 0:
        prefix_sum[i + 1] = 0
        count += 1
    else:
        prefix_sum[i + 1] = nums[i] + prefix_sum[i]

if count == n:
    print(max(nums))
else:
    print(max(prefix_sum))
