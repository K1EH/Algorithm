def sieve(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    primes = [p for p, v in enumerate(is_prime) if v]
    return primes


PRIME_LIMIT = 1_000_000
primes = sieve(PRIME_LIMIT)
3
N = int(input())
for _ in range(N):
    num = int(input())
    if num <= PRIME_LIMIT:
        print("NO")
        continue
    for p in primes:
        if num % p == 0:
            print("NO")
            break
    else:
        print("YES")
