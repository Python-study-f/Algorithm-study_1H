def dfs(x,y):
    if x == N -1 and y == M-1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if data[nx][ny] < data[x][y]:
                    dp[x][y] += dfs(nx,ny)
    return dp[x][y]


dx = [0,0,-1,1] # L,R,U,D
dy = [-1,1,0,0]


N, M = map(int,input().split())
data = [[] for _ in range(N)]
for i in range(N):
    data[i] = list(map(int,input().split()))
# 입력값 설정 및 초기화
dp = [[-1]*M for _ in range(N)]

print(dfs(0,0))

