import sys
input = sys.stdin.readline
N = int(input())

arr = list(map(int, input().split()))
arr_s = sorted(list(set(arr)))

res = {arr_s[i] : i for i in range(len(arr_s))}
for a in arr:
    print(res[a], end = " ")