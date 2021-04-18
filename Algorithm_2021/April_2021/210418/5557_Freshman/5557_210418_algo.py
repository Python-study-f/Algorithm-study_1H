n = int(input())
nums = [0]+list(map(int,input().split()))
dp = [[0]*21 for _ in range(n+1)]
dp[1][nums[1]] = 1

for i in range(2,n):
    for j in range(21):
        if dp[i-1][j]:
            if nums[i]+j<=20:
                dp[i][j+nums[i]] += dp[i-1][j]
            if 0<=j-nums[i]:
                dp[i][j-nums[i]] += dp[i-1][j]

print(dp[n-1][nums[-1]])
