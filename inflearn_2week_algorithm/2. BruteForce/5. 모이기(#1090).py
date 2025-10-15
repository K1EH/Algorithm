N = int(input())
pos = [list(map(int, input().split())) for _ in range(N)]

ys = sorted(list(y for y, x in pos))
xs = sorted(list(x for y, x in pos))

y = ys[len(ys) // 2]
x = xs[len(xs) // 2]

# Only one person
dist2mid = []
# More than two people
for p in pos:
    dx, dy = p
    dist2mid.append(abs(x - dx) + abs(y - dy))
dist2mid.sort()

ans = []
r_sum = 0
for d in dist2mid:
    r_sum += d
    ans.append(sum)
ans[0] = 0
print(*ans)
