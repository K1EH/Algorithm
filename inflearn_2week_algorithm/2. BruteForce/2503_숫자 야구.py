N = int(input())
guesses = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a == b or b == c or c == a:
                continue
            target = str(a * 100 + b * 10 + c)
            count = 0
            for guess in guesses:
                strike_count = 0
                ball_count = 0
                g = str(guess[0])
                strike = guess[1]
                ball = guess[2]
                for i in range(3):
                    if g[i] == target[i]:
                        strike_count += 1
                    if g[i] in target:
                        ball_count += 1
                if strike_count == strike and ball_count - strike_count == ball:
                    count += 1
            if count == N:
                ans += 1
print(ans)
