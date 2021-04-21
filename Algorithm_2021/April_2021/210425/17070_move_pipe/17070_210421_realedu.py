"""
DFS, BFS풀이 모두 시간초과 (pypy3에서도 마찬가지)
-> DP를 이용해야 시간안에 해결 가능
from collections import deque

dy = [0, 1, 1]
dx = [1, 0, 1]

N = int(input())
# MAP = list(map(int, input().split()) for _ in range(N))
MAP = [list(map(int, input().split())) for _ in range(N)]
# print(MAP)
a, b, state = 0, 1, 0 # 끝점 기준으로
result = 0

def dfs(a, b, dir):
    global MAP, result
    Q = deque()
    Q.append([a, b, dir])

    # 끝점 도착
    while Q:
        y, x, dir = Q.popleft() #

        if y == N-1 and x == N-1:
            result += 1

        for i in range(3):
            # print(i)
            # 가로인 파이프에 세로 파이프 X / 세로인 파이프에 가로 파이프 X
            if ((i == 0 and dir == 1) or (i == 1 and dir == 0)):
                continue

            ny = y + dy[i]
            nx = x + dx[i]

            if ny >= N or nx >= N or MAP[ny][nx] == 1:
                continue

            if i == 2 and (MAP[y][x + 1] == 1 or MAP[y + 1][x] == 1):
                continue

            """
            if 0 <= ny < N and 0 <= nx < N:
                if MAP[ny][nx] == 0:
                    # if MAP[ny][nx] == 0:
                    Q.append([ny, nx, i])
                    # Q.append([ny, nx, i])
            """
            Q.append([ny, nx, i])
            
dfs(a, b, state)
print(result)
"""


import sys
input = sys.stdin.readline


N = int(input())

MAP = [list(map(int, input().split())) for _ in range(N)]
board = [[[0]*3 for _ in range(N)] for _ in range(N)]
board[0][1][0] = 1

for i in range(2, N):
    if MAP[0][i] == 0:
        board[0][i][0] = board[0][i-1][0]

# 이동
for y in range(N):
    for x in range(2, N):
        # 대각선 이동 경우의 수
        if MAP[y][x] == 0 and MAP[y][x - 1] == 0 and MAP[y-1][x] == 0:
            board[y][x][2] = board[y-1][x-1][0] + board[y-1][x-1][1] + board[y-1][x-1][2]

        # 나머지 가로, 세로 이동 경우의 수
        if MAP[y][x] == 0:
            # 가로 이동
            board[y][x][0] = board[y][x-1][2] + board[y][x-1][0]
            # 세로 이동
            board[y][x][1] = board[y-1][x][2] + board[y-1][x][1]

print(board[N-1][N-1][0] + board[N-1][N-1][1] + board[N-1][N-1][2])
            
