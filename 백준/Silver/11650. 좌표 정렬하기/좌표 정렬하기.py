import sys
input = sys.stdin.readline
N = int(input())
l = []
for i in range(N):
    l.append(list(map(int, input().split())))
l.sort()


for i in range(N):
    print(*l[i])