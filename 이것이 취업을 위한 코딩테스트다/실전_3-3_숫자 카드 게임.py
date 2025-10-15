# V1, 시간복잡도 : O(N*M log M) (정렬 때문에)
N, M = map(int, input().split())
cards = [sorted(list(map(int, input().split()))) for _ in range(N)]

print(max(cards, key=lambda x: x[0])[0])

# V2, 시간복잡도 : O(N*M)
N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]

max_num = 0
for c in cards:
    if max_num < min(c):
        max_num = min(c)

print(max_num)

"""
Input 1
3 3
3 1 2
4 1 4
2 2 2
Output 1
2
Input 1
2 4
7 3 1 8
3 3 3 4
Output 1
3
"""
