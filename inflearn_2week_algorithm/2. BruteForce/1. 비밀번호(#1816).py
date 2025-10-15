TC = int(input())

for _ in range(TC):
    num = int(input())
    if num < 1_000_001:
        print("NO")
    else:
        for pf in range(2, 1_000_001):
            if num % pf == 0:
                print("NO")
                break
        else:
            print("YES")
