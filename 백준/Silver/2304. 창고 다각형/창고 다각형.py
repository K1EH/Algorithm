def area(arr):
    a = 0
    location, height = arr[0]
    for L, H in arr[1:]:
        if H >= height:
            a += abs(L - location) * height
            location, height = L, H
    return a


N = int(input())
ans = 0
columns = [list(map(int, input().split())) for _ in range(N)]
columns.sort()

idx = columns.index(max(columns, key=lambda x: x[1]))

left_columns = columns[: idx + 1]
right_columns = columns[idx:][::-1]

ans = area(left_columns) + area(right_columns) + columns[idx][1]
print(ans)
