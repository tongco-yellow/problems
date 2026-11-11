# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 = progresses <100 (작업의 진도)
# 작업의 개발 속도가 적힌 정수 배열 = speeds /< 100 (작업의 속도)
# 각 배포다 마다 몇개의 기능이 배포되는지를 return
# 제한 사항 : 배포는 하루에 한 번만.

# 93퍼 스피드 1 = 7일 걸림 ___ 30퍼 스피드 30 =3일 -> 7일째 배포 ___55퍼 스피드 5 = 9일간 작업 후
#= return 7일째에 2개 9일째에 1개

def solution(progresses, speeds):
    answer = []
    dayss = []

    for i in range(len(progresses)):
        progress = progresses[i]
        day = 0

        while progress < 100:
            progress += speeds[i]
            day += 1

        dayss.append(day)

    current = dayss[0]
    count = 1

    for i in range(1, len(dayss)):
        if dayss[i] <= current:
            count += 1
        else:
            answer.append(count)
            current = dayss[i]
            count = 1

    answer.append(count)

    return answer
            
        
    