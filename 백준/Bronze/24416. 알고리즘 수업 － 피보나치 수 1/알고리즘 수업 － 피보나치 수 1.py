def fib(n):
    global count
    if n == 1 or n == 2:
        return 1
    else:
        count += 1
        return fib(n - 1) + fib(n - 2)

n = int(input())
count = 1
fib(n)
print(count, n - 2)
