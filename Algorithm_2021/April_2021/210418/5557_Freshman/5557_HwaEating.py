n = int(input())
arr = list(map(int,input().split()))
query = arr.pop()
dp = [[0]*21 for _ in range(n-1)]
dp[0][arr[0]] = 1
for i in range(1,n-1):
    su = arr[i]
    for j in range(21):
        if dp[i-1][j]:
            if j-su >= 0:
                dp[i][j-su] += dp[i-1][j]
            if j+su < 21:
                dp[i][j+su] += dp[i-1][j]

print(dp[n-2][query])
