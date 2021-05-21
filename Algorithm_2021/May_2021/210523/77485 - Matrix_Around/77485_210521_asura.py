def solution(rows, columns, queries):
    board = [[0] * (columns + 1) for _ in range(rows +1)]
    n=1
    ans = []

    for i in range(1,rows+1): # 인덱스를 더 쉽게 처리하기 위한 보드 생성
        for j in range(1,columns+1):
            board[i][j] = n
            n += 1

    for query in queries:

        x1,y1,x2,y2 = query
        tmp = board[x2][y2]
        board_min = int(1e9)


        for i in range(x2,x1,-1):
            board[i][y2] = board[i-1][y2]
            board_min = min(board_min,board[i][y2])

        for i in range(y2,y1,-1):
            board[x1][i] = board[x1][i-1]
            board_min = min(board_min,board[x1][i])

        for i in range(x1,x2):
            board[i][y1] = board[i+1][y1]
            board_min = min(board_min,board[i][y1])

        for i in range(y1,y2):
            board[x2][i] = board[x2][i+1]
            if i == y2-1:
                board[x2][i] = tmp
            board_min = min(board_min,board[x2][i])
        ans.append(board_min)

    return ans

