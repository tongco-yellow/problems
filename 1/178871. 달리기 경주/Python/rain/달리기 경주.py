def solution(players, callings):
    rank = {}

    for i in range(len(players)):
        rank[players[i]] = i

    for name in callings:
        i = rank[name]

        front = players[i - 1]

        players[i - 1], players[i] = players[i], players[i - 1]

        rank[name] -= 1
        rank[front] += 1

    return players
