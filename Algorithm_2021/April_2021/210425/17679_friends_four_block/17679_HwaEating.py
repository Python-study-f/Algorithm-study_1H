def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]
    flag = True
    delete = []
    while flag:
        flag = False
        for i in range(m-1):
            for j in range(n-1):
                target = board[i][j]
                if not target:
                    continue
                cnt = 0
                for x in range(2):
                    for y in range(2):
                        if board[i+x][j+y] == target:
                            cnt += 1
                if cnt == 4:
                    for x in range(2):
                        for y in range(2):
                            delete.append([i+x,j+y])
        if delete:
            flag = True
            while delete:
                x,y = delete.pop()
                if board[x][y]:
                    board[x][y] = ''
                    answer += 1
                    
        for j in range(n):
            stack = []
            for i in range(m):
                if board[i][j]:
                    stack.append(board[i][j])
                    board[i][j] = ''
            base = m-1
            while stack:
                board[base][j] = stack.pop()
                base -= 1
            
    return answer

m,n = 4,5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m,n,board))