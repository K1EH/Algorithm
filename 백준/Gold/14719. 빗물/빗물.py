def water(arr):
    res = 0
    std = arr[0]
    for block in arr[1:]:
        if std < block:
            std = block
        else:
            res += std - block
    return res


H, W = map(int, input().split())
blocks = list(map(int, input().split()))

idx = blocks.index(max(blocks))
left_blocks = blocks[: idx + 1]
right_blocks = blocks[idx:][::-1]

ans = water(left_blocks) + water(right_blocks)
print(ans)
