def solution(board, h, w):
    answer = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        if (h + dy[i] >= 0) and (h + dy[i] < len(board)) and (w + dx[i] >= 0) and (w + dx[i] < len(board)):
            if board[h][w] == board[h+dy[i]][w+dx[i]]:
                answer += 1
    
    return answer