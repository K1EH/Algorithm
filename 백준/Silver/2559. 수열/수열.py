N, interval = map(int, input().split())

days = list(map(int, input().split()))
prefix = [0 for _ in range(N + 1)]
for i in range(N):
    prefix[i + 1] = prefix[i] + days[i]

interval_sum = []
for i in range(interval, N + 1):
    interval_sum.append(prefix[i] - prefix[i - interval])

print(max(interval_sum))
