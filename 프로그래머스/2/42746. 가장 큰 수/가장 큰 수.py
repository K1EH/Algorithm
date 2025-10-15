def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers.sort(key = lambda x: x*4, reverse = True)
    for w in numbers:
        answer += w
    return str(int(answer))