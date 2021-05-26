N = int(input())
arr = []
for i in range(N):
    n = int(input())
    arr.append(n)

dp = [1]*N

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))

# LIS 알고리즘 : 최장 증가 수열 구하기
# 1. dp 2. binary search  3. brute force 
