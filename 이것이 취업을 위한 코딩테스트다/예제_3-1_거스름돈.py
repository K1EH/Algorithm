# 동전의 큰 단위가 항상 작은 단위의 배수이므로 -> Greedy Algorithm
# 화폐 단위가 무작위로 주어진 경우 -> Dynamic Programming
coins = [500, 100, 50, 10]
N = int(input())
count = 0
for coin in coins:
    count += N // coin
    N %= coin
print(count)
