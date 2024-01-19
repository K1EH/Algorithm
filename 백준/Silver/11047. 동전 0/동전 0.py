N, K = map(int, input().split())
coins = []
count = 0
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse = True)
for coin in coins:
    count += K // coin
    K %= coin
print(count)