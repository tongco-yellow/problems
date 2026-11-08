def solution(numbers):
    answer = set()

    def dfs(start, total, count):
        if count == 2:
            answer.add(total)
            return

        for i in range(start, len(numbers)):
            dfs(i + 1, total + numbers[i], count + 1)

    dfs(0, 0, 0)
    return sorted(answer)
