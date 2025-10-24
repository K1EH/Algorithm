def hanoi(N, start, end, temp):
    if N == 1:
        print(start, end)
    else:
        hanoi(N - 1, start, temp, end)
        print(start, end)
        hanoi(N - 1, temp, end, start)


N = int(input())
print(2**N - 1)
hanoi(N, 1, 3, 2)
