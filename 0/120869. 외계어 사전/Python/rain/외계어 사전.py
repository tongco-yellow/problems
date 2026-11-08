
def solution(spell, dic):
    answer = 2
    visited = [False] * len(spell)

    def dfs(word):
        nonlocal answer

        if len(word) == len(spell):
            if word in dic:
                answer = 1
            return

        for i in range(len(spell)):
            if not visited[i]:
                visited[i] = True
                dfs(word + spell[i])
                visited[i] = False

    dfs("")
    return answer
