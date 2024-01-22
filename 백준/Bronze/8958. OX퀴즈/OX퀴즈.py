N = int(input())

for _ in range(N):
    ans = input()

    score = 1
    total = 0
    for i in range(len(ans)):
        if ans[i] == 'O':
            total += score
            score += 1
        else:
            score = 1
    print(total)