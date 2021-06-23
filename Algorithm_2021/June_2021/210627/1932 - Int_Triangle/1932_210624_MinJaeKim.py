n = int(input())
dp = [0]*n
for i in range(n):
    L = [*map(int, input().split())]
    for j in range(i, -1, -1):
        if j ==0:
            dp[j]+=L[j]
        elif j==n-1:
            dp[j]= dp[j-1]+L[j]
        else:
            dp[j] = max(dp[j-1]+L[j], dp[j]+L[j])
print(max(dp))
