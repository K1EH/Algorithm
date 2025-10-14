N = int(input())
columns = [list(map(int, input().split())) for _ in range(N)]
columns.sort(key=lambda x: x[0])

ml, mh = max(columns, key=lambda x: x[1])

ll, lh, rl, rh = 0, 0, 1000, 0
area = 0

for l in range(N):
    cl, ch = columns[l]
    if lh < ch:
        area += (cl - ll) * lh
        ll, lh = cl, ch
    if ch == mh:
        break
for r in range(N - 1, -1, -1):
    cl, ch = columns[r]
    if rh < ch:
        area += (rl - cl) * rh
        rl, rh = cl, ch
    if ch == mh:
        break
area += (rl - ll + 1) * mh
print(area)
