n, m = map(int, input().split())
mp = [list(map(int, list(input()))) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if mp[i][j] == 1:
            dp[i][j] = 1
            ans = 1

for i in range(1, n):
    for j in range(1, m):
        if mp[i][j] == 1:
            dp[i][j] += min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        ans = max(ans, dp[i][j])
print(ans*ans)
