candy = int(input())
ans = 0
# an even number of candies
for c in range(2, candy + 1, 2):
    for b in range(1, (candy - c) + 1):
        if candy - b - c >= b + 2:
            ans += 1
print(ans)
