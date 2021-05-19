TC = int(input())

for _ in range(TC):
    N = int(input())
    data = []
    dp = [[0] * N for _ in range(2)]

    for _ in range(2):
        data.append(list(map(int, input().split())))

    dp[0][0] = data[0][0]
    dp[1][0] = data[1][0]

    for i in range(1, N):
        dp[0][i] = max(data[0][i] + dp[1][i - 1], dp[0][i - 1]) # 이때, i-2가 아니라 i-1인 이유는 i-1의 dp의 값이 현재 dp의 값과 같다.
        dp[1][i] = max(data[1][i] + dp[0][i - 1], dp[1][i - 1])

    print(max(dp[0][N - 1], dp[1][N - 1]))