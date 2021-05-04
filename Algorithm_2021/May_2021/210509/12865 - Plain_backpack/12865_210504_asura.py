N, K = map(int,input().split()) # N은 tot 물품수, K는 Max weight

knapsack = [[0,0]]
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(N):
    knapsack.append(list(map(int,input().split())))

for i in range(1,N+1):
    for j in range(1,K+1):
        if j >= knapsack[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-knapsack[i][0]] + knapsack[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])