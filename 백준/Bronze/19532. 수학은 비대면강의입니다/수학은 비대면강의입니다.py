a, b, c, d, e, f = map(int, input().split())
for x in range(-999, 1000):
    if b != 0:
        if (c - a * x) / b == (c - a * x) // b:
            y = (c - a * x) // b
            if d * x + e * y == f:
                print(x, y)
                break
    else:
        x = c // a
        y = (f - d * x) // e
        print(x, y)
        break