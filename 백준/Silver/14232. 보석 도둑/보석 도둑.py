def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for prime in range(2, int(n**0.5) + 1):
        if is_prime[prime]:
            for multiple in range(prime * prime, n + 1, prime):
                is_prime[multiple] = False
    return [i for i, v in enumerate(is_prime) if v]


ans = []
k = int(input())
primes = sieve(int(k**0.5) + 1)
for prime in primes:
    while k % prime == 0:
        ans.append(prime)
        k //= prime

if k != 1:
    ans.append(k)
print(len(ans))
print(*ans)
