from collections import Counter

def solution(topping):
    
    n = len(topping)
    answer = 0
    set_left = set()
    count_right = Counter(topping)
    len_right = len(count_right)
    
    for i in range(n):
        set_left.add(topping[i])
        count_right[topping[i]] -= 1
        if count_right[topping[i]] == 0:
            len_right -= 1
        if len(set_left) == len_right:
            answer += 1
    return answer