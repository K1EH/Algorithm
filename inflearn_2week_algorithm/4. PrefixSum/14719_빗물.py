H, W = map(int, input().split())
cols = list(map(int, input().split()))

drops = 0

for i in range(1, W - 1):
    left_wall, right_wall = max(cols[0:i]), max(cols[i + 1 :])
    if cols[i] < left_wall and cols[i] < right_wall:
        drops += min(left_wall, right_wall) - cols[i]

print(drops)
