from itertools import product
N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
for i in product(arr, repeat = M):
    print(*i)