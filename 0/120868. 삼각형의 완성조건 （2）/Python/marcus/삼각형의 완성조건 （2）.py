def solution(sides):
    answer = 0
    idx = 0
    idxb = 0
    big = 0
    sht = 0
    for a in range(2):
        if sides[a] > big:
            big = sides[a]
            idx = a
    if idx == 0:
        idxb = 1
    sht = sides[idxb]
    
    answer += 2 * sht - 1
    return answer