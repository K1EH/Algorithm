N = int(input())
case = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a == b or b == c or c == a:
                continue
            target = str(100 * a + 10 * b + c)

            count = 0
            for i in range(N):
                ball_count = 0
                strike_count = 0

                guess = str(case[i][0])
                strike = case[i][1]
                ball = case[i][2]
                for j in range(3):
                    # ball check
                    if guess[j] in target:
                        ball_count += 1
                    # strike check
                    if guess[j] == target[j]:
                        strike_count += 1
                if ball_count - strike_count == ball and strike_count == strike:
                    count += 1
            if count == N:
                ans += 1
print(ans)
