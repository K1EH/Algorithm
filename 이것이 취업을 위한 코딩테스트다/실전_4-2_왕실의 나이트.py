pos = input()
directions = ((2, 1), (2, -1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (-1, -2))

x, y = ord(pos[0]) - ord("a") + 1, int(pos[1])
count = 0
for direction in directions:
    dy, dx = direction
    if 1 <= x + dx <= 8 and 1 <= y + dy <= 8:
        count += 1
print(count)
