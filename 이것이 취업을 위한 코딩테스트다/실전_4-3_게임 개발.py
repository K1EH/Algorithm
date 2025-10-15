# 북쪽 기준 탐색 순서 (좌-하-우-상)
N, M = map(int, input().split())
x, y, d = map(int, input().split())
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
directions = directions[d:] + directions[:d]
x, y = x - 1, y - 1
grid = [list(map(int, input().split())) for _ in range(N)]

"""
상 : 좌-하-우-상
우 : 상-좌-우-하
하 : 우-상-좌-하
좌 : 하-우-상-좌
"""
"""
Input
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
Output
3
"""
