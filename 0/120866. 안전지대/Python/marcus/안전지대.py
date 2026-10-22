def solution(board):
    dxs = [1, 1, 0, -1, -1, -1, 0, 1]
    dys = [0, 1, 1, 1, 0, -1, -1, -1]
    answer = 0
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1 or board[i][j] == 2:
                continue
            for a in range(0, 8):
                if (i + dxs[a] >= 0 and j + dys[a] >= 0) and (i + dxs[a] < len(board) and j + dys[a] < len(board)):
                    if board[i+dxs[a]][j+dys[a]] == 1:
                        board[i][j] = 2
                        break
            if board[i][j] == 0:
                answer += 1

    return answer