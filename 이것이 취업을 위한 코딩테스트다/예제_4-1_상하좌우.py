directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
N = int(input())
moves = list(map(str, input().split()))
pos = (1, 1)
for move in moves:
    dx, dy = directions[move]
    x, y = pos
    nx, ny = x + dx, y + dy
    if 1 <= nx <= N and 1 <= ny <= N:
        pos = (nx, ny)
print(*pos)


"""
Input
5
R R R U D D
Output
3 4
"""
