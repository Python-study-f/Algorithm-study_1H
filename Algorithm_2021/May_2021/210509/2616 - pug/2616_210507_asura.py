'''
https://lyzqm.blogspot.com/2017/03/2616.html
https://stillchobo.tistory.com/110
2차원 DP가 가장 어려운 거 같다 ㅠㅠ... 다시 풀어보고 개인 블로그에 정리하자
점화식 : dp [i][j] = max( dp[i][j-1], sum [j] - sum [j-floor] + dp [i-1][j-floor] )
'''

N = int(input())
data = list(map(int,input().split()))
floor = int(input())

dp = [[int(-1e9)] * 50001 for _ in range(4)] # 2차원 DP. 소형 기관차 i개 있고 + 객실이 총 j개까지 있을때 최대 승객 수
index_sum = [0 for _ in range(50001)] #

for i in range(1,N+1):
    index_sum[i] = index_sum[i-1] + data[i-1]

for i in range(1,4):
    for j in range(i*floor,N+1):
        if i == 1:
            dp[i][j] = max(dp[i][j-1], index_sum[j] - index_sum[j-floor])
        else:
            dp[i][j] = max(dp[i][j-1], index_sum[j] - index_sum[j-floor] + dp[i-1][j-floor])

print(dp[3][N])