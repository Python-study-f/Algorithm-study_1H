
N= int(input())
mp=[]
mp.append([0]*(N+2))
mp+= [[0]+[*map(int, input().split())]+ [0] for _ in range(N)]
mp.append([0]*(N+2))

dp= [[[0]*3 for _ in range(N+2)] for __ in range(N+2)] # 가로 세로 대각선

mp[1][1]=1
dp[1][2][0]=1
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==1 and j==2: continue
        if mp[i][j]==0:
            dp[i][j][0]=dp[i][j-1][0] +dp[i][j-1][2]
            dp[i][j][1]=dp[i-1][j][1] +dp[i-1][j][2]
            dp[i][j][2]=(dp[i-1][j-1][0]+dp[i-1][j-1][1]+ dp[i-1][j-1][2] if mp[i-1][j]==0 and mp[i][j-1]==0 else 0)


print(sum(dp[N][N]))
            