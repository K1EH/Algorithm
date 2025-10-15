N = int(input())
triangle = []

for _ in range(N):
    triangle.append(list(map(int, input().split())))
for i in range(1, N):
    for k in range(i+1):
        if k == 0:
            triangle[i][k] += triangle[i-1][k]
        elif k == i:
            triangle[i][k] += triangle[i-1][k-1]
        else:
            triangle[i][k] += max(triangle[i-1][k], triangle[i-1][k-1])
print(max(triangle[N - 1]))