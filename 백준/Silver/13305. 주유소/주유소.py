N = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

gas = []
res = 0
min = cost[0]

# 1. 모든 주유소의 리터당 가격은 1원이다.
if sum(cost) == N:
    print(sum(road))
else:
    for i in range(N - 1):
        if min > cost[i]:
            min = cost[i]
        res += road[i] * min
    print(res)