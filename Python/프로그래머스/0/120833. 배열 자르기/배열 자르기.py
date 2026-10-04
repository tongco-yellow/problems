def solution(numbers, num1, num2):
    result=[]

    for i in numbers[num1:num2+1] :
        result.append(i)
    return result