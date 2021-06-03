# 주지수 15724 백준

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

# 행 더하기
for i in range(n):
    for j in range(1, m):
        board[i][j] += board[i][j - 1]

# 열 더하기
for i in range(m):
    for j in range(1, n):
        board[j][i] += board[j - 1][i]

board.insert(0, [0] * m)

for i in board:
    i.insert(0, 0)

k = int(input())

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    print(board[x2][y2] - board[x1 - 1][y2] - board[x2][y1 - 1] + board[x1 - 1][y1 - 1])
