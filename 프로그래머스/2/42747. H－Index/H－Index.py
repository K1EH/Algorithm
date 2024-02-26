def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for idx in range(len(citations)):
        if idx + 1 <= citations[idx]:
            answer = idx + 1
    return answer