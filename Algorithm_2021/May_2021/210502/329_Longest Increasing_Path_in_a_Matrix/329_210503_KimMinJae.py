def longestIncreasingPath(matrix):
    Dy= [0,0,1,-1]
    Dx= [1,-1,0,0]
    n= len(matrix)
    m= len(matrix[0])
    dp=[[0]*m for _ in range(n)]
    ans=0
    def travel(y, x,matrix,dp):
        if dp[y][x]:
            return dp[y][x]
        mx=0
        for dy, dx in zip(Dy, Dx):
            ny= y+ dy
            nx= x+ dx
            if 0<=ny<n and 0<=nx<m and matrix[ny][nx]>matrix[y][x]:
                mx= max(mx,travel(ny, nx,matrix,dp))
        dp[y][x]= mx+1
        return dp[y][x]
    
    for i in range(n):
        for j in range(m):
            dp[i][j]= travel(i,j,matrix,dp)
            ans=max(ans,dp[i][j])
    return ans