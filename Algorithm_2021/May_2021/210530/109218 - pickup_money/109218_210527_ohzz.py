# 주울 수 있는 최대 돈 109218 구름

n = int(input())

money = list(map(int, input().split()))
dp = [0] * n

dp[0] = money[0]
dp[1] = money[0] + money[1]
dp[2] = max(dp[1], max(money[1] + money[2], dp[0] + money[2]))

for i in range(3, n):
    dp[i] = max(dp[i - 1], max(dp[i - 3] + money[i - 1] + money[i], dp[i - 2] + money[i]))

print(dp[n - 1])
