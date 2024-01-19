N = int(input())
meetings = []

for _ in range(N):
    meetings.append(list(map(int, input().split())))

# 끝나는 시간을 기준으로 오름차순 정렬
meetings.sort(key=lambda x: (x[1], x[0]))
end_time = meetings[0][1]
count = 1
for meeting in meetings[1::]:
    if meeting[0] == meeting[1]:
        count += 1
    elif end_time <= meeting[0]:
        count += 1
        end_time = meeting[1]
print(count)
