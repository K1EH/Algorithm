list = []
for i in range(5):
    list.append(int(input()))

list.sort()
print(sum(list)//5)
print(list[2])