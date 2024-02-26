def solution(progresses, speeds):
    answer = []
    count = 0
    while progresses:
        if progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            continue
        if count:
            answer.append(count)
        count = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
    if count:
            answer.append(count)
        
    return answer