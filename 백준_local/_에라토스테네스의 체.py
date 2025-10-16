def sieve(N):
    is_prime = [True] * (N + 1)
    # 0 and 1 is not a prime number
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(N**0.5) + 1):
        # if 'i' is prime number
        if is_prime[i]:
            # from 'i*i' to 'N + 1' aren't prime numbers
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    primes = [p for p, v in enumerate(is_prime) if v]
    return primes


print(sieve(5))
