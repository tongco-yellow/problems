def solution(keymap, targets):
    answer = []

    for target in targets:
        total = 0

        for char in target:
            count = 101

            for key in keymap:
                if char in key:
                    count = min(count, key.index(char) + 1)

            if count == 101:
                total = -1
                break

            total += count

        answer.append(total)

    return answer
