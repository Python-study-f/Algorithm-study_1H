N = int(input())
num = []
dp = []
for _ in range(N):
    num.append(list(map(int, input().split())))
    dp.append([0]*N)
dp[0][0] = num[0][0]
for i in range(N-1):
    for j in range(i+1):
         dp[i+1][j] = max(dp[i][j] + num[i+1][j], dp[i+1][j])
         dp[i+1][j+1] = max(dp[i][j] + num[i+1][j+1], dp[i+1][j+1])

result = 0
for i in range(N):
    result = max(result, dp[N-1][i])

print(result)

