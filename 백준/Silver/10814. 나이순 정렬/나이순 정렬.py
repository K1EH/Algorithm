import sys
input = sys.stdin.readline

N = int(input())
member = [list(input().split()) for _ in range(N)]
member.sort(key = lambda x : int(x[0]))
for _ in member:
    print(*_)