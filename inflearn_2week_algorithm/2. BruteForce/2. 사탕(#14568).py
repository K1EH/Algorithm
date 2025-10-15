candies = int(input())
count = 0
for c in range(2, candies + 1, 2):
    # 1. Distribute candies for C
    last = candies - c
    if last >= 3:
        # 2. Distribute candies for A and B
        for b in range(1, (last - 2) // 2 + 1):
            a = last - b
            if a - b >= 2:
                count += 1
print(count)
