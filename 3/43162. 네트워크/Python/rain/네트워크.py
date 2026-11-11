# 컴퓨터의 개수 n, 
# 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 
# 1/< n /<200
# 각 컴퓨터는 0부터 n-1인 정수로 표현??????


def solution(n, computers):
    answer = 0

    def dfs(i):
        for j in range(n):
            if computers[i][j] == 1:
                computers[i][j] = 0
                computers[j][i] = 0
                dfs(j)

    for i in range(n):
        if 1 in computers[i]:
            dfs(i)
            answer += 1

    return answer

