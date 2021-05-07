n, k = map(int, input().split())

weight_value = [(0, 0)]

for i in range(n):
    w, v = map(int, input().split())
    weight_value.append((w, v))
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= weight_value[i][0]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight_value[i][0]] + weight_value[i][1])
        else:
            dp[i][j] = dp[i - 1][j]
           
print(dp[n][k])
