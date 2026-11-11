def solution(n, computers):
    passed = [False] * n
    answer = 0
    def dfs(a, b):
        passed[b] = True
        for i in range(n):
            if computers[b][i] == 1 and passed[i] == False:
                dfs(b, i)
    
    for j in range(n):
        for k in range(j, n):
            if computers[j][k] == 1 and passed[k] == False:
                dfs(j, k)
                answer += 1
    return answer