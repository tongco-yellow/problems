def solution(n, computers):
    passed = [False] * n
    answer = 0
    def dfs(a, b):
        passed[b] = True
        for k in range(n):
            if computers[b][k] == 1 and passed[k] == False:
                dfs(b, k)
    
    for i in range(n):
        for j in range(i, n):
            if computers[i][j] == 1 and passed[j] == False:
                dfs(i, j)
                answer += 1
    return answer