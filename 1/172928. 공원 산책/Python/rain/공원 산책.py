
def solution(park, routes):
    x, y = 0, 0

    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                x, y = i, j

    direction = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }

    for route in routes:
        d, n = route.split()
        n = int(n)

        dx, dy = direction[d]

        nx, ny = x, y

        for _ in range(n):
            nx += dx
            ny += dy

            if not (0 <= nx < len(park) and 0 <= ny < len(park[0])):
                break

            if park[nx][ny] == "X":
                break

        else:
            x, y = nx, ny

    return [x, y]
