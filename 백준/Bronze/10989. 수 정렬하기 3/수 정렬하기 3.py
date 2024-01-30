import sys
input = sys.stdin.readline

N = int(input())
index = [0] * 10000
for _ in range(N):
    index[int(input()) - 1] += 1
for _ in range(10000):
    if index[_] != 0:
        for i in range(index[_]):
            print(_  + 1)