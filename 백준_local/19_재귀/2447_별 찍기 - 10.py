def blank(square, start, length):
    if length == 1:
        return
    ys, xs = start
    third = length // 3
    for y in range(ys + third, ys + third * 2):
        for x in range(xs + third, xs + third * 2):
            square[y][x] = " "
    for y in range(ys, ys + length, third):
        for x in range(xs, xs + length, third):
            if not (y == (ys + third) and x == (xs + third)):
                blank(square, (y, x), third)


length = int(input())
square = list(["*"] * length for _ in range(length))

blank(square, (0, 0), length)
for s in square:
    print("".join(s))
