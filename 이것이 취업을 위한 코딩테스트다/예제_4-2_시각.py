N = int(input())
NIN3 = 1575
IN3 = 3600
if N < 3:
    hour = N + 1
elif N < 13:
    hour = N
elif N < 23:
    hour = N - 1
else:
    hour = N - 2
print(hour * NIN3 + (N + 1 - hour) * IN3)
