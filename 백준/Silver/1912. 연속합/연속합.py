INF = 1e9

N = int(input())
arr = list(map(int, input().split()))
prefix = [-INF for _ in range(N + 1)]
for i in range(N):
    prefix[i + 1] = max(arr[i] + prefix[i], arr[i])

print(max(prefix))
