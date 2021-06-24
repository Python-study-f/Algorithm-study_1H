# 정수 삼각형 1932 백준

import sys

input = sys.stdin.readline

n = int(input())

dp = [[0] * n for _ in range(n)]
dp[0][0] = int(input())

for i in range(1, n):
    tmp = list(map(int, input().split()))
    length = len(tmp)
    dp[i][0] = dp[i - 1][0] + tmp[0]
    dp[i][length - 1] = dp[i - 1][length - 2] + tmp[-1]
    for j in range(1, len(tmp) - 1):
        dp[i][j] = max(dp[i - 1][j - 1] + tmp[j], dp[i - 1][j] + tmp[j])

print(max(dp[-1]))
