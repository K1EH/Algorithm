def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for prime in range(2, int(n**0.5)):
        if is_prime[prime]:
            for multiple in range(prime**2, n + 1, prime):
                is_prime[multiple] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

N = int(input())
primes = sieve(int(N**0.5) + 1)
for prime in primes:
    while N % prime == 0:
        print(prime)
        N //= prime
if N != 1:
    print(N)