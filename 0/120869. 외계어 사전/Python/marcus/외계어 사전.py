def solution(spell, dic):
    answer = 2
    for i in dic:
        counting = 0
        for k in spell:
            if i.count(k) == 0:
                counting = 0
                break
            else:
                counting += i.count(k)
        if counting == len(i):
            answer = 1
            break
    return answer