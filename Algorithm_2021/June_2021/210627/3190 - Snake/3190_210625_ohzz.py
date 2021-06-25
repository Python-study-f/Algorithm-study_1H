# 뱀 3190 백준

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

board = [[0] * n for _ in range(n)]

for i in range(k):
    ax, ay = map(int, input().split())
    board[ax - 1][ay - 1] = 1

l = int(input())

timedir = []
for i in range(l):
    timedir.append(input().split())


def rotate(dir, c):
    if c == "D":
        dir = (dir + 1) % 4
    else:
        dir = (dir - 1) % 4
    return dir


# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

snakeDir = 0
time = 1
x, y = 0, 0
check = deque()
check.append([x, y])
board[x][y] = 2

while True:
    x, y = x + dx[snakeDir], y + dy[snakeDir]
    if 0 <= x < n and 0 <= y < n and board[x][y] != 2:
        if board[x][y] != 1:
            tailX, tailY = check.popleft()
            board[tailX][tailY] = 0
        check.append([x, y])
        board[x][y] = 2
        for td in timedir:
            if time == int(td[0]):
                snakeDir = rotate(snakeDir, td[1])
        time += 1
    else:
        break

print(time)
