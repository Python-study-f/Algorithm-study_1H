for t in range(int(input())):
    n = int(input())
    stk1 = [0]+[i for i in list(map(int,input().split()))]
    stk2 = [0]+[i for i in list(map(int,input().split()))]
    mx = 0
    dp = [[0]*(n+1), [0]*(n+1)]
    dp[0][1] = stk1[0]
    dp[1][1] = stk2[0]
    for i in range(1,n+1):
        dp[0][i] = max(dp[1][i-2],dp[1][i-1]) + stk1[i]
        dp[1][i] = max(dp[0][i-2],dp[0][i-1]) + stk2[i]
        if dp[0][i] > mx:
            mx = dp[0][i]
        if dp[1][i] > mx:
            mx = dp[1][i]

    print(mx)