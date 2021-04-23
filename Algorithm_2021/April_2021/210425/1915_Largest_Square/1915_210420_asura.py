# 프로그래머스에서 풀어본 기억이 있음
# 좌측 상단부터 우측 하단으로 검색을 하므로 L,U 는 신경 안쓰고
# R,D 그리고 대각선만 신경쓰면서 DP로 문제 풀면 됨
# BFS로 계층적으로 count 떄려도 될 거 같음.

N, M = map(int,input().split())

data = [[] for _ in range(N)]

for i in range(N):
    data[i] = list(map(int,input()))

dp = [[0] * M for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        if data[i][j] != 0: # 어차피 인덱스 넘어가더라더 dp를 맨처음에 0으로 초기화해서 전혀 상관X
                dp[i][j] =min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        ans = max(dp[i][j], ans)

print(ans**2)
