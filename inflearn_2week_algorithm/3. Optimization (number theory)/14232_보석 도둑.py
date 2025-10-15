def sieve(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N**0.5)):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    prime = [p for p, v in enumerate(is_prime) if v]
    return prime


ans = []
N = int(input())
prime = sieve(int(N**0.5) + 1)
for p in prime:
    while N % p == 0:
        N //= p
        ans.append(p)
if N != 1:
    ans.append(N)
print(len(ans))
print(*ans)
