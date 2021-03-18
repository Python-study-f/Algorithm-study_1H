import sys
input = sys.stdin.readline
n = int(input())
t = [0]*(n+1)
p = [0]*(n+1)

for i in range(n):
    a,b = map(int,input().split())
    t[i] = a
    p[i] = b

dp = [0]*(n+1)

for i in range(n+1):
    if i:
        dp[i] = max(dp[i-1],dp[i])
    if i + t[i] > n:
        continue
    dp[i+t[i]] = max(dp[i]+p[i], dp[i+t[i]])

print(dp[n])