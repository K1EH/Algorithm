ans = 0
H, W = map(int, input().split())
blocks = list(map(int, input().split()))

for i in range(1, len(blocks) - 1):
    ans += max(0, min(max(blocks[:i]), max(blocks[i + 1 :])) - blocks[i])
print(ans)
