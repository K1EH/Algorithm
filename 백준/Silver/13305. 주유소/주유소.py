N = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

gas = []
res = 0
if sum(cost) == N:
    print(sum(road))
else:
    for i in range(N - 1):
        gas.append(cost[i])
        res += road[i] * min(gas)
    print(res)