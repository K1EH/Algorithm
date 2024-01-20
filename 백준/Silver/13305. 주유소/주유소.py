N = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

gas = []
res = 0
for i in range(N - 1):
    gas.append(cost[i])
    res += road[i] * min(gas)
print(res)