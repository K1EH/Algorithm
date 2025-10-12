PRIME_LIMIT = 1_000_000

N = int(input())
for _ in range(N):
    num = int(input())
    if num <= PRIME_LIMIT:
        print("NO")
        continue
    for p in range(2, PRIME_LIMIT + 1):
        if num % p == 0:
            print("NO")
            break
    else:
        print("YES")
