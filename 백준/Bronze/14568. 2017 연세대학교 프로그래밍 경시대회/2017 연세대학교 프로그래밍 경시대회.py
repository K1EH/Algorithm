candy = int(input())
count = 0
if candy >= 6:
    for c in range(2, candy + 1, 2):
        for b in range(1, candy + 1 - c):
            a = candy - c - b

            if a >= b + 2 and a > 0:
                count += 1
print(count)