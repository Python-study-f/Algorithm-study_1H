# 구간 합 구하기 11660 백준
n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# 행 더하기
for i in range(n):
    for j in range(1, n):
        board[i][j] += board[i][j - 1]

# 열 더하기
for i in range(n):
    for j in range(1, n):
        board[j][i] += board[j - 1][i]


for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(board[x2][y2] - board[x1 - 1][y2] - board[x2][y1 - 1] + board[x1 - 1][y1 - 1])
