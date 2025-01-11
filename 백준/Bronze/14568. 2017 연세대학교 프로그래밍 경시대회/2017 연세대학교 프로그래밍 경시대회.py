N = int(input())

count = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if i + j + k == N:
                if k % 2 == 0:
                    if i >= j + 2:
                        count += 1
print(count)
