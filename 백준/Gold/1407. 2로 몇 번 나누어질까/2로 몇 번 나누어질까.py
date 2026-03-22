global ARR
ARR = [2**i for i in range(1, 51)]


def div_2(n):
    ans = 0
    for i in range(len(ARR) - 1):
        ans += (n // ARR[i] - n // ARR[i + 1]) * ARR[i]
    if n % 2 == 0:
        ans += n // 2
    else:
        ans += n // 2 + 1
    return ans


A, B = map(int, input().split())
print(div_2(B) - div_2(A - 1))
