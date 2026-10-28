def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        added = 0
        ifrange = False
        minimum = 0
        for j in range(queries[i][0], queries[i][1] + 1):
            if arr[j] > queries[i][2]:
                if not ifrange:
                    ifrange = True
                    minimum = arr[j]
                else:
                    if minimum > arr[j]:
                        minimum = arr[j]
        if not ifrange:
            answer.append(-1)
        else:
            answer.append(minimum)
        
    return answer