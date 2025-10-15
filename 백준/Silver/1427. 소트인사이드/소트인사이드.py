num = input()
arr = []
for i in range(len(num)):
    arr.append(num[i])
arr.sort(reverse=True)
for i in arr:
    print(i, end="")