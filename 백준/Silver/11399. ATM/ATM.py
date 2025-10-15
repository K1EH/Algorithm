N = int(input())
people = list(map(int, input().split()))
people.sort(reverse=True)

res = 0
for i in range(1, N + 1):
    res += i * people[i - 1]
print(res)