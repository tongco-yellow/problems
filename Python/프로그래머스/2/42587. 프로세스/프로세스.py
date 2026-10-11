def solution(priorities, location):
    queue = []
    count = 0

    for i in range(len(priorities)):
        queue.append([priorities[i], i])

    while len(queue) > 0:
        current = queue.pop(0)
        higher = False

        for item in queue:
            if item[0] > current[0]:
                higher = True
                break

        if higher:
            queue.append(current)

        else:
            count += 1

            if current[1] == location:
                return count