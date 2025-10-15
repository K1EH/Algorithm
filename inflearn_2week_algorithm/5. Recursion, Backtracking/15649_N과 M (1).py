N, M = map(int, input().split())

result = []

def dfs():
    if len(result) == M:
        print(*result)
        return
    
    for i in range(1, N + 1):
        if i not in result:    # 중복 방지
            result.append(i)
            print(f"append: {result}")
            dfs()              # 재귀 호출
            result.pop()       # 백트래킹
            print(f"pop: {result}")

dfs()