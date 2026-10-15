def solution(X, Y):
    answer = ""
    for i in range(10):
        j = 9 - i
        count_x = X.count(str(j))
        count_y = Y.count(str(j))
        count = min(count_x, count_y)
        for _ in range(count):
            answer += str(j)

    if not answer:
        return "-1"
    if answer[0] == "0":
        return "0"
    return answer