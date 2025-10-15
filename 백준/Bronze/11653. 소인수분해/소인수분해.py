def sieve(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    prime = [i for i, p in enumerate(is_prime) if p]
    return prime


N = int(input())
prime = sieve(int(N ** 0.5) + 1)
idx = 0

for p in prime:
    while N % p == 0:
        print(p)
        N //= p

if N!= 1:
    print(N)
