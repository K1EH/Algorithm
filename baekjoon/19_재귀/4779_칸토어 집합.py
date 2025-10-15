def recursion(N, start, end, line):
    if N == 1:
        return
    third = (end - start + 1) // 3
    line[start + third : start + 2 * third] = " " * third
    recursion(third, start, start + third - 1, line)
    recursion(third, start + 2 * third, end, line)


while True:
    try:
        N = int(input())
        line = ["-"] * (3**N)
        recursion(3**N, 0, 3**N - 1, line)
        print("".join(line))
    except:
        break