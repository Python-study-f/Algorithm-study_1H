
# 생각해보면 DFS로 접근하면 2^100 이므로 시간초과가 날 수밖에 없다. 그렇다면 BFS 또한 안될것이므로
# 예를들어 8,3 으로 만들 수 있는 경우의 수는 5,11 -> 8,3,2 으로 만들 수 있는 경우의 수 => 3,7,9,13 ...
# 즉 작은문제로 큰 문제를 해결할 수 있을 거 같으므로 바로 DP로 접근하면 된다.
# 또한, 이전 숫자의 정보도 가지고 있어야 하므로 1차원이 아닌 2차원 dp로 구현
# dp[i][j] = i번쨰까지 연산하고 나서, j값을 가질 수 있는 수

N = int(input())
data = list(map(int,input().split()))

dp = [[0] * 21 for _ in range(N-1)] # (0~20) * N만큼의 2차원 list
dp[0][data[0]] = 1

for i in range(1,N-1):
    for j in range(21):
        if dp[i-1][j] != 0:

            pos = j
            cur = data[i]

            if 0<= pos + cur <= 20:
                dp[i][pos+cur] += dp[i-1][pos]

            if 0 <= pos - cur <= 20:
                dp[i][pos - cur] += dp[i - 1][pos]

print(dp[-1][data[-1]])


# 1. 단순 DFS => 시간초과
'''
N = input()
data = list(map(int,input().split()))
target = data[-1]

ans = 0

def dfs(tar,tot,i):
    global ans

    if i > len(data)-1:
        return

    if tot == tar and i == len(data)-1: # data의 마지막 값 빼야함
        ans += 1
        return

    if  tot < 0 or tot > 20 : # 0과 20사이가 아닐 경우
        return

    dfs(tar,tot+data[i],i+1)
    dfs(tar,tot-data[i],i+1)

first_data = data[0]
dfs(target,first_data,1)

print(ans)
'''
