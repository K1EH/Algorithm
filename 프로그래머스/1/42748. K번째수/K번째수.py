def solution(array, commands):
    answer = []
    for a, b, c in commands:
        arr = array[a-1: b]
        arr.sort()
        answer.append(arr[c-1])
    return answer