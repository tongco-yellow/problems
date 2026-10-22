def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        counting = 0
        for j in range(len(name)):
            if name[j] in photo[i]:
                counting += yearning[j]
        answer.append(counting)
    
    return answer