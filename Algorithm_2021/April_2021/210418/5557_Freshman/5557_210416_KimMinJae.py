import sys; input= lambda: sys.stdin.readline().rstrip()
n=int(input())
MX=20
L=[*map(int, input().split())]
dp= [[0]*(MX+1) for _ in range(n)]
dp[0][L[0]]=1
for i in range(1,n-1):
    for j in range(MX+1):
        if dp[i-1][j]: 
            if j+L[i]<=20:
                dp[i][j+L[i]]+= dp[i-1][j]
            if 0<=j-L[i]:
                dp[i][j-L[i]]+= dp[i-1][j]
print(dp[n-2][L[-1]])