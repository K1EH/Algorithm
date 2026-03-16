N = int(input())
# target, strike, ball
li = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a == b or b == c or c == a:
                continue
            for l in li:
                st, ba = 0, 0
                target, strike, ball = l
                x, y, z = target // 100, target // 10 % 10, target % 10

                for i, j in zip([a, b, c], [x, y, z]):
                    if i == j:
                        st += 1
                    if j in [a, b, c]:
                        ba += 1
                ba -= st
                if not (st == strike and ba == ball):
                    break
            else:
                answer += 1

print(answer)
