answer = 0
def solution(numbers, target):
    evrnum = [numbers, [-num for num in numbers]]
    def dfs(x, collect):
        global answer
        if x == len(numbers):
            if collect == target:
                answer += 1
        else:
            for i in range(2):
                dfs(x+1, collect + evrnum[i][x])
    dfs(0, 0)
    
    return answer