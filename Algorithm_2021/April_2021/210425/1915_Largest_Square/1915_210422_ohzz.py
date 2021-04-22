# 가장 큰 정사각형 1915

n, m = map(int, input().split())

board = [list(map(int, list(input()))) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

maxValue = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            tmp = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
            dp[i][j] = tmp + 1
            if maxValue < dp[i][j]:
                maxValue = dp[i][j]

print(maxValue * maxValue)

# 42서울 마지막 과제랑 비슷했음.
