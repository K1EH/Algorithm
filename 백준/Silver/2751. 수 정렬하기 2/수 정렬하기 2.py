import sys
input = sys.stdin.readline

N = int(input())
list = (int(input()) for _ in range(N))
a = sorted(list)

for _ in a:
    print(_)