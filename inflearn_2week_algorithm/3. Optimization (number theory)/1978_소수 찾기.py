def sieve(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(N**0.5 + 1)):
        if is_prime:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    return is_prime


ans = 0
N = int(input())
nums = list(map(int, input().split()))

is_prime = sieve(max(nums))
for num in nums:
    if is_prime[num]:
        ans += 1
print(ans)
