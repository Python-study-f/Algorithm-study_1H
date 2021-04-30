# 비숍 1799 백준

# 틀린 코드

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
checkBoard = [[0] * n for _ in range(n)]

res = 0
dx = [-1, -1]
dy = [1, -1]


def check(row, col):
    for i in range(2):
        nx = row
        ny = col
        while True:
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                break
            if checkBoard[nx][ny]:
                return False
            nx += dx[i]
            ny += dy[i]
    return True


def bishopCheck(arr):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
    return cnt


def dfs(row, col):
    global res
    if row == n - 1 and col == n:
        res = max(res, bishopCheck(checkBoard))
        return
    else:
        if check(row, col) and board[row][col] == 1:
            checkBoard[row][col] = 1
            dfs2(row, col + 1)
            checkBoard[row][col] = 0
        else:
            dfs2(row, col + 1)


def dfs2(row, col):
    if row == n - 1 and col == n:
        dfs(row, col)
    elif col == n:
        dfs2(row + 1, 0)
    else:
        dfs(row, col)


dfs(0, 0)
print(res)
