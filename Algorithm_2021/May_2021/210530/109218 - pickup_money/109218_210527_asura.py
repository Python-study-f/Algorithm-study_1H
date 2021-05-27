N = int(input())
data = list(map(int,input().split()))
dp = [0] * N

dp[0] = data[0]
dp[1] = data[0] + data[1] # 돈의 액수가 1<= M <= 10이므로 
dp[2] = max(data[0] + data[2] , data[1] + data[2], data[1])


for i in range(3,N):
	# i번쨰 줍는경우, i번째 줍지 않는 경우
	dp[i] = max(dp[i-3] + data[i-1] + data[i], dp[i-2] + data[i], dp[i-1]) 

print(max(dp))