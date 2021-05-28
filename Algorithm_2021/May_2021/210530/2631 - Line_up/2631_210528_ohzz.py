# 줄세우기 2631 백준

n = int(input())
arr = []
dp = [1] * n
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
