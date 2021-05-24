import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y,h):
    for dic in range(4):
        nx,ny = x + dx[dic], y + dy[dic]

        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] > h and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny,h)



# 입력 #
N = int(input())
board = [[] for _ in range(N)]
for i in range(N):
    board[i] = list(map(int,input().split()))
#======#


max_area = -int(1e9)


for tc in range(101): # 총 높이
    cnt = 0
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] > tc and not visited[i][j]:
                visited[i][j] = True
                cnt += 1
                dfs(i,j,tc)

    max_area = max(max_area,cnt)

print(max_area)

