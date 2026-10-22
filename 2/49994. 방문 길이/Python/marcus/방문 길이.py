def passed(start, end, route):
    if len(route) == 1:
        return False
    for i in range(len(route) - 1):
        if route[i] == start:
            if route[i + 1] == end:
                return True
        if route[i] == end:
            if route[i + 1] == start:
                return True
    return False


def solution(dirs):
    answer = 0
    route = []
    a = 0
    b = 0
    route.append((a, b))
    for dir in dirs:
        c = a
        d = b
        if dir == 'U':
            b += 1
        if dir == 'D':
            b -= 1
        if dir == 'R':
            a += 1
        if dir == 'L':
            a -= 1
        if (a > 5) or (a < -5) or (b > 5) or (b < -5):
            a = c
            b = d
            continue
        if not passed((c, d), (a, b), route):
            answer += 1
        route.append((a, b))
    
    return answer