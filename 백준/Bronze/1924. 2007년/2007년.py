day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

x, y = map(int, input().split())
temp = 0
for i in range(x - 1):
    temp += month[i]
temp += y
print(day[temp % 7])