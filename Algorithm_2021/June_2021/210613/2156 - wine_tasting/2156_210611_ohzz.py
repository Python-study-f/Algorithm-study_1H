# 포도주 시식 2156 백준

import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * n
arr = []
for i in range(n):
    arr.append(int(input()))

if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0] + arr[1])
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(dp[1], max(arr[1] + arr[2], dp[0] + arr[2]))

    for k in range(3, n):
        dp[k] = max(dp[k - 1], max(dp[k - 3] + arr[k - 1] + arr[k], dp[k - 2] + arr[k]))

    print(dp[n - 1])
