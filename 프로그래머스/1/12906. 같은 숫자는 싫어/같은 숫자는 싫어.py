def solution(arr):
    answer = []
    prev = arr[0]
    arr.append(-1)
    for i in range(1, len(arr)):
        if arr[i] == prev:
            continue
        else:
            answer.append(prev)
            prev = arr[i]
    return answer