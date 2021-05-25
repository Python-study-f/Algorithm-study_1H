N = int(input())
arr = list(map(int, input().split()))

if N == 1:
    print(arr[0])
elif N == 2:
    print(arr[0] + arr[1])
elif N == 3:
    print(max(arr[0] + arr[1], arr[1] + arr[2], arr[0] + arr[2]))
else:
    dp = [0] * len(arr)
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])

    for i in range(3, len(arr)):
        dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i], dp[i-1])

    print(dp[N-1])
