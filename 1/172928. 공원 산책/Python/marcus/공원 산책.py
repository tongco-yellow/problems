def solution(park, routes):
    garo = len(park[0])
    sero = len(park)
    for a in range(sero):
        for b in range(garo):
            if park[a][b] == 'S':
                hit = a
                wdt = b
    
    for i in range(len(routes)):
        drt, amt = routes[i].split()
        amt = int(amt)
        cantpass = False
        if drt == 'E':
            if not wdt + amt >= garo:
                for j in range(amt+1):
                    if park[hit][wdt+j] == 'X':
                        cantpass = True
                        break
                if not cantpass:
                    wdt += amt
        if drt == 'S':
            if not hit + amt >= sero:
                for j in range(amt+1):
                    if park[hit+j][wdt] == 'X':
                        cantpass = True
                        break
                if not cantpass:
                    hit += amt
        if drt == 'W':
            if not wdt - amt < 0:
                for j in range(amt+1):
                    if park[hit][wdt-j] == 'X':
                        cantpass = True
                        break
                if not cantpass:
                    wdt -= amt
        if drt == 'N':
            if not hit - amt < 0:
                for j in range(amt+1):
                    if park[hit-j][wdt] == 'X':
                        cantpass = True
                        break
                if not cantpass:
                    hit -= amt
    answer = [hit, wdt]
    return answer