T = int(input())
#dp[i][0]: 2*(i+1) 스티커, 마지막 뗀 스티커가 위일때 최대합
#dp[i][1]: 2*(i+1) 스티커, 마지막 뗀 스티커가 아래일때 최대합

for _ in range(T):
    n = int(input())
    L=[0,0]
    L[0]=[int(i) for i in input().split()] #윗줄
    L[1]=[int(i) for i in input().split()] #아랫줄

    dp=[]
    dp=[[0,0], [L[0][0], L[1][0]]]
    for i in range(2,n+1):
        dp.append([max(dp[i-1][1],dp[i-2][0],dp[i-2][1])+L[0][i-1], max(dp[i-1][0],dp[i-2][0],dp[i-2][1])+L[1][i-1]])

    print(max(dp[n])) # max 인데 min으로 잘못넣음