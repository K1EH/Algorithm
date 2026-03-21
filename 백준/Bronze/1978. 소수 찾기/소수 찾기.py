def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for prime in range(2, int(n**0.5)):
        if is_prime[prime]:
            for multiple in range(prime * prime, n + 1, prime):
                is_prime[multiple] = False
    return is_prime


is_prime = sieve(1_000)
N = int(input())
arr = list(map(int, input().split()))
count = 0
for i in arr:
    if is_prime[i]:
        count += 1
print(count)
