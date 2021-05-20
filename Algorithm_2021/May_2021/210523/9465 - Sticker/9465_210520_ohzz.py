# 스티커 9465 백준

T = int(input())

for _ in range(T):
    n = int(input())
    dp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        dp[i] = dp[i] + list(map(int, input().split()))

    for j in range(2, n + 2):
        for i in range(2):
            if i == 0:
                dp[i][j] = dp[i][j] + max(dp[i + 1][j - 1], dp[i + 1][j - 2])
            else:
                dp[i][j] = dp[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j - 2])

    print(max(dp[0][n + 1], dp[1][n + 1]))
