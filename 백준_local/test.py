d = int(input())
directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
a = "북동서남"
for i in range(d - 1, d - 5, -1):
    d=(d + 3) % 4
    print(directions[i], a[i])
    print("방향",d)
