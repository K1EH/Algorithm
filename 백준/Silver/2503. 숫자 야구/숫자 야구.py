N = int(input())

answer = 0

hint = list(list(map(int, input().split())) for _ in range(N))

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a == b or b == c or c == a:
                continue
            count = 0
            for arr in hint:
                strike_count = 0
                ball_count = 0
                num = arr[0]
                strike = arr[1]
                ball = arr[2]

                first = num // 100
                second = (num // 10) % 10
                third = num % 10

                ### strike, ball 검증 ###
                if a == first:
                    strike_count += 1
                elif a in [second, third]:
                    ball_count += 1
                if b == second:
                    strike_count += 1
                elif b in [first, third]:
                    ball_count += 1
                if c == third:
                    strike_count += 1
                elif c in [first, second]:
                    ball_count += 1

                if strike == strike_count and ball == ball_count:
                    count += 1
            if N == count:
                answer += 1
print(answer)
