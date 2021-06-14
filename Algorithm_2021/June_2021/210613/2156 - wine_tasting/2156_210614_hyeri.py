N = int(input())
dp = [0]*(N+1)
arr = [0]
for _ in range(N):
    arr.append(int(input()))
if N == 1:
    print(arr[1])
else:
    dp[1] = arr[1]
    dp[2] = dp[1] + arr[2]
    
    for i in range(3, N+1):
        dp[i] = max(arr[i]+arr[i-1]+dp[i-3], arr[i]+dp[i-2])
        dp[i] = max(dp[i], dp[i-1])

    print(dp[N])

