dx = [0,0,-1,1] # L,R,U,D
dy = [-1,1,0,0]


def dfs(x,y,change,tot):
    global ans,K
    ans = max(ans,tot)
    visit[x][y] = True

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < N and 0 <= ny < N:
            if not visit[nx][ny]:
                if board[nx][ny] < board[x][y]:
                    dfs(nx,ny,change,tot+1)
                elif not change and (board[nx][ny] - board[x][y] < K):
                    tmp = board[nx][ny]
                    board[nx][ny] = board[x][y] - 1
                    dfs(nx,ny,True,tot+1)
                    board[nx][ny] = tmp
    visit[x][y] = False



TC = int(input())

for tc in range(1,TC+1):
    N,K = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]

    height_max = max(map(max,board)) # 최대높이 구하기. 이거 어떻게하면 효율적으로 구할까요..

    ans = 1
    for i in range(N):
        for j in range(N):
            if board[i][j] == height_max:
                visit = [[False] * N for _ in range(N)]
                dfs(i,j,False,1)

    print(f'#{tc} {ans}')
