T = int(input())

for t in range(T):
    n = int(input())

    sticker = [[0] * 2 for _ in range(2)]
    for i in range(2):
        sticker[i] = sticker[i] + list(map(int, input().split()))
    dp = [[0] * (n+2) for _ in range(2)]

    for i in range(2, n+2):
        dp[0][i] = max(max(dp[0][i - 1], dp[1][i - 1] + sticker[0][i]), dp[1][i - 2] + sticker[0][i]);
        dp[1][i] = max(max(dp[1][i - 1], dp[0][i - 1] + sticker[1][i]), dp[0][i - 2] + sticker[1][i]);

    if dp[0][n+1] > dp[1][n+1]:
        print(str(dp[0][n+1]))
    else:
        print(str(dp[1][n+1]))
