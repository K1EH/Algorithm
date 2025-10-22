def recursion(line, N):
    if N - 1 < 0:
        return line
    erase = 3 ** (N - 1)
    left = line[:erase]
    mid = [" "] * erase
    right = line[erase * 2 :]
    return recursion(left, N - 1) + mid + recursion(right, N - 1)


while True:
    try:
        N = int(input())
        line = ["-"] * (3**N)
        print("".join(recursion(line, N)))
    except:
        exit(0)
