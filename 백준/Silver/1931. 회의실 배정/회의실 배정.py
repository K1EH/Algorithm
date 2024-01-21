N = int(input())

meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))

meetings.sort(key = lambda x: (x[1], x[0]))

end = meetings[0][1]
count = 1
for meeting in meetings[1:]:
    if end <= meeting[0]:
        count += 1
        end = meeting[1]
print(count)