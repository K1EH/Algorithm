N = int(input())
li = []
count = 0
for _ in range(N):
    li.append(list(map(int, input().split())))
for case in range(123, 999):
    case = str(case)
    if (
        case[0] == case[1]
        or case[1] == case[2]
        or case[2] == case[0]
        or case[0] == '0'
        or case[1] == '0'
        or case[2] == '0'
    ):
        continue
    for guess, strike, ball in li:
        (
            s,
            b,
        ) = (
            0,
            0,
        )
        guess = str(guess)
        for i in range(3):
            if case[i] == guess[i]:
                s += 1
            if guess[i] in case:
                b += 1
        if strike != s or ball != b - s:
            break
    else:
        count += 1
print(count)
