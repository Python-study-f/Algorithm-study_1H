N = int(input())
board = [[] for _ in range(N)]

for i in range(N):
    board[i] = list(map(int,input().split()))

dp = [[0] * N for _ in range(N)]
dp[0][0] = board[0][0]


for i in range(N):
    for j in range(0,i+1):
        dp[i][j] = board[i][j] + max(dp[i-1][j-1],dp[i-1][j])
        # 점화식

print(max(dp[N-1]))