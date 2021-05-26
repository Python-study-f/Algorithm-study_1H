# 안전영역 2468 백준

import sys

n = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sys.setrecursionlimit(10 ** 6)
ans = 0
cnt = 0
maxValue = 0

board = [list(map(int, input().split())) for _ in range(n)]


def checkIndex(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


def dfs(x, y, h):
    checkBoard[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if checkIndex(xx, yy) and checkBoard[xx][yy] == 0 and board[xx][yy] > h:
            dfs(xx, yy, h)


for i in range(n):
    tmp = max(board[i])
    maxValue = max(tmp, maxValue)

for h in range(maxValue):
    checkBoard = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if checkBoard[i][j] == 0 and board[i][j] > h:
                cnt += 1
                dfs(i, j, h)
    ans = max(cnt, ans)

print(ans)
