ans = -1e9

N, K = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0 for _ in range(N + 1)]

for i in range(N):
    prefix[i + 1] = prefix[i] + arr[i]

for i in range(K, N + 1):
    temp = prefix[i] - prefix[i - K]
    if ans < temp:
        ans = temp
print(ans)
