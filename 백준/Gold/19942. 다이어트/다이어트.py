N = int(input())
minimum = list(map(int, input().split()))
ingredient = [list(map(int, input().split())) for _ in range(N)]

answer = []


def recursion(idx, arr, cost, numbers):
    global answer
    if idx == N:
        for i in range(4):
            if not (arr[i] >= minimum[i]):
                break
        else:
            answer.append([cost, numbers])
        return

    recursion(
        idx + 1,
        [arr[i] + ingredient[idx][i] for i in range(4)],
        cost + ingredient[idx][4],
        numbers + [idx + 1],
    )
    recursion(
        idx + 1,
        arr,
        cost,
        numbers,
    )


recursion(0, [0, 0, 0, 0], 0, [])
answer.sort()
if answer:
    print(answer[0][0])
    print(*answer[0][1])
else:
    print(-1)
