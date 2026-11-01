#반복문 없이 재귀로만 풀어보기

def solution(n):
    def factorial(i, result):
        if result > n:
            return i - 1

        return factorial(i + 1, result * (i + 1))

    return factorial(1, 1)
