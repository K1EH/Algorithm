expression = input()
expression += '+'
li = []
num = ''
for i in range(len(expression)):
    if expression[i] in ['+', '-']:
        li.append(num)
        li.append(expression[i])
        num = ''
    else:
        num += expression[i]
res = int(li[0])
li = li[::-1]
temp = 0
for i in li[0:-1]:
    if i == '-':
        res -= temp
        temp = 0
    elif i != '+':
        temp += int(i)
res += temp
print(res)
