def dfs(x,y):
    if x == n-1 and y == m-1:
        dp[x][y] = 1
        return 1
    dp[x][y] = 0
    for i in range(4):
        xi, yi = x+dx[i], y+dy[i]
        if 0<=xi<n and 0<=yi<m and arr[x][y] > arr[xi][yi]:
            if dp[xi][yi] >= 0:
                dp[x][y] += dp[xi][yi]
            else:
                dp[x][y] += dfs(xi,yi)
    return dp[x][y]
        
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
print(dfs(0,0))
