N = int(input())
arrN = list(map(int, input().split()))
arrN = set(sorted(arrN))
M = int(input())
arrM= list(map(int, input().split()))

for i in arrM:
    if i in arrN:
        print(1)
    else:
        print(0)