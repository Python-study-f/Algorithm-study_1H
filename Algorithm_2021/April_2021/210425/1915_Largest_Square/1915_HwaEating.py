dx = [-1,-1,0]
dy = [-1,0,-1]
n,m = map(int,input().split())
arr = [list(map(int,list(input()))) for _ in range(n)]

dp = [i[:] for i in arr]
ans = 0
for i in range(n):
    for j in range(m):
        if dp[i][j] == 0:
            continue
        mn = 1001
        for p in range(3):
            xi, yi = i + dx[p], j + dy[p]
            if 0<=xi<n and 0<=yi<m:
                mn = min(mn, dp[xi][yi])
            else:
                mn = 0
                break
        dp[i][j] = mn + 1
        ans = max(ans, dp[i][j])

print(ans**2)

