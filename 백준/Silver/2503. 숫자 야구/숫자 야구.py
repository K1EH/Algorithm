global count
count = 0

N = int(input())
hint = [list(map(int, input().split())) for _ in range(N)]
arr = []
visited = [False] * 10


def recursion():
    global count
    if len(arr) == 3:
        for num, strike, ball in hint:
            s, b = 0, 0
            num_li = [num // 100, num // 10 % 10, num % 10]
            for j in range(3):
                if arr[j] == num_li[j]:
                    s += 1
                elif arr[j] in num_li:
                    b += 1
            if not (s == strike and b == ball):
                break
        else:
            count += 1
        return

    for i in range(1, 10):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            recursion()
            arr.pop()
            visited[i] = False


recursion()
print(count)
