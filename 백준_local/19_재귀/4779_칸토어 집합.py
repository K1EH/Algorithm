def recursion(line, start, length):
    if length == 0:
        return
    third = length // 3
    for i in range(start + third, start + third * 2):
        line[i] = " "
    recursion(line, start, third)
    recursion(line, start + third * 2, third)


while True:
    try:
        N = int(input())
        line = ["-"] * (3**N)
        recursion(line, 0, len(line))
        print("".join(line))
    except:
        exit(0)
