N = int(input())
pos = [list(map(int, input().split())) for _ in range(N)]
min_x = min(pos, key=lambda x: x[0])[0]
min_y = min(pos, key=lambda x: x[1])[1]

for p in pos:
    print(p)
for i in range(N):
    pos[i][0] -= min_x
    pos[i][1] -= min_y
for p in pos:
    print(p)

# X값 증감 -> 수평선분
# Y값 증감 -> 수직선분
grid = [0] * (max())