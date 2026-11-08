
def solution(word):
    answer = 0
    ahdma= "AEIOU"

    def dfs(current):
        nonlocal answer

        if current == word:
            return True

        if len(current) == 5:
            return False

        for v in ahdma:
            answer += 1

            if dfs(current + v):
                return True

        return False

    dfs("")
    return answer
