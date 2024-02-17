dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        if dp[20][20][20]:
            return dp[20][20][20]
        else:
            dp[20][20][20] = w(20, 20, 20)
            return dp[20][20][20]
    elif a < b and b < c:
        if dp[a][b][c-1]: o = dp[a][b][c-1]
        else: o = w(a, b, c-1)
        if dp[a][b-1][c-1]: p = dp[a][b-1][c-1]
        else: p = w(a, b, c-1)
        if dp[a][b-1][c]: q = dp[a][b-1][c]
        else: q = w(a, b-1, c) 
        dp[a][b][c] = o + p - q
    else:
        if dp[a-1][b][c]: o = dp[a-1][b][c]
        else: o = w(a-1, b, c)
        if dp[a-1][b-1][c]: p = dp[a-1][b-1][c]
        else: p = w(a-1, b-1, c)
        if dp[a-1][b][c-1]: q = dp[a-1][b][c-1]
        else: q = w(a-1, b, c-1)
        if dp[a-1][b-1][c-1]: r = dp[a-1][b-1][c-1]
        else: r = w(a-1, b-1, c-1)
        dp[a][b][c] = o + p + q - r
    return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
