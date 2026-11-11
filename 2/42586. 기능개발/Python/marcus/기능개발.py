def solution(progresses, speeds):
    due_day = []
    for i in range(len(progresses)):
        due_day.append((100 - progresses[i]) // speeds[i])
        if ((100 - progresses[i]) % speeds[i]) != 0:
            due_day[i] += 1
        
    answer = []
    max = 0
    for j in due_day:
        if max < j:
            answer.append(1)
            max = j
        else:
            answer[-1] += 1
    
    return answer