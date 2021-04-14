n = int(input())
numbers = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n)]

dp[0][numbers[0]] = 1

for i in range(1, n - 1):
    for j in range(21):
        if dp[i - 1][j] > 0:
            if j + numbers[i] <= 20:
                dp[i][j + numbers[i]] += dp[i - 1][j]
            if j - numbers[i] >= 0:
                dp[i][j - numbers[i]] += dp[i - 1][j]

# for i in range(n):
#     print(dp[i])

print(dp[len(numbers) - 2][numbers[len(numbers) - 1]])

# https://dev-wd.github.io/algorithm/backjoon5557/ 이 그림 보고 이해함.
