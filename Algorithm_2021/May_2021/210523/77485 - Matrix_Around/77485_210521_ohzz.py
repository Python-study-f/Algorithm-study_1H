# 행렬 테두리 회전하기 77485 프로그래머스


def turnBoard(x1, y1, x2, y2, board):
    tmp = board[x1][y1]
    res = board[x1][y1]

    for i in range(x1, x2):
        board[i][y1] = board[i + 1][y1]
        res = min(res, board[i][y1])

    for j in range(y1, y2):
        board[x2][j] = board[x2][j + 1]
        res = min(res, board[x2][j])

    for k in range(x2, x1, -1):
        board[k][y2] = board[k - 1][y2]
        res = min(res, board[k][y2])

    for m in range(y2, y1, -1):
        board[x1][m] = board[x1][m - 1]
        res = min(res, board[x1][m])
    board[x1][m] = tmp

    return res


def solution(row, columns, queries):
    answer = []
    board = []
    cnt = 0
    for _ in range(row):
        tmp = []
        for _ in range(columns):
            cnt += 1
            tmp.append(cnt)
        board.append(tmp)
    for i in range(len(queries)):
        answer.append(
            turnBoard(
                queries[i][0] - 1, queries[i][1] - 1, queries[i][2] - 1, queries[i][3] - 1, board
            )
        )

    return answer


# row = 6
# columns = 6
# query = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]

# print(solution(row, columns, query))
