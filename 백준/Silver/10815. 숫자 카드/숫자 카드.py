import sys
input = sys.stdin.readline

N = int(input())
# 상근이 카드
sang_card = set(map(int, input().split()))

M = int(input())
# 숫자 카드
num_card = list(map(int, input().split()))

for num in num_card:
    if num in sang_card:
        print(1, end = " ")
    else:
        print(0, end = " ")