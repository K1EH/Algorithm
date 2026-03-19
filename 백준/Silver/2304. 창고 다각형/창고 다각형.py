N = int(input())
ans = 0
columns = []
for _ in range(N):
    columns.append(list(map(int, input().split())))
columns.sort()


idx = columns.index(max(columns, key=lambda x: x[1]))
left_columns = columns[: idx + 1]
right_columns = sorted(columns[idx:], reverse=True)

for col in [left_columns, right_columns]:
    pos, height = col[0]
    for p, h in col[1:]:
        if h >= height:
            ans += abs(p - pos) * height
            pos, height = p, h
print(ans + columns[idx][1])
