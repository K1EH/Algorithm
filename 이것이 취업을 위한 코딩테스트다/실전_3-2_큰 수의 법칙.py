"""
Input
5 8 3
2 4 5 4 6
Output
46
"""

N, M, K = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort(reverse=True)
cycle = M // (K + 1)
remain = M % (K + 1)

ans = cycle * (nums[0] * K + nums[1]) + remain * (nums[0])

print(ans)
