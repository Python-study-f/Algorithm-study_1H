n= int(input())
k= int(input())
M=int(1e9)+3
dp= [[0]*(k+1) for _ in range(n)]
for i in range(1,n):
    dp[i][1]=1
for i in range(1,n):
    for a in range(1,k+1):
        if i-2>=0:
            dp[i][a]+=dp[i-2][a-1]
            dp[i][a]%=M
    for a in range(1,k+1):
        dp[i][a]+=dp[i-1][a]
        dp[i][a]%=M
        
#print(dp)
red= [[0]*(k+1) for _ in range(n)]
red[0][1]=1
for i in range(n-1):
    for a in range(1,k+1):
        if i-2>=0:
            red[i][a]+=red[i-2][a-1]
            red[i][a]%=M
    for a in range(1,k+1):
        red[i][a]+=red[i-1][a]
        red[i][a]%=M
#print(red)

ans=dp[n-1][k]+red[n-2][k]
ans%=M
print(ans)