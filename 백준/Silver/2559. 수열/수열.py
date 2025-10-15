n, interval = map(int, input().split())

temperature = list(map(int, input().split()))

prefix_sum = [0 for _ in range(n + 1)]

for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + temperature[i]
if interval == 1:
    print(max(temperature))

else:
    max = -1e9
    for p in range(interval, n + 1):
        temp = prefix_sum[p] - prefix_sum[p - interval]
        if max < temp:
            max = temp
    print(max)
