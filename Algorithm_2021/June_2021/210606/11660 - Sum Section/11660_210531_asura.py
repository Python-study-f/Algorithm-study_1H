import sys

input = sys.stdin.readline

#1. Brute-Force = 시간초과
'''
N, M = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    data = list(map(lambda x: sum(x[y1-1:y2]), board[x1-1:x2]))
    print(sum(data))
'''

#2. DP
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
lst_point = [list(map(int,input().split())) for _ in range(M)]

dp = [[0] * (N+1) for _ in range(N+1)]



for i in range(1, N+1):  # 전체 DP
    for j in range(1, N+1):
        # 여기서 board[i-1][j-1] 현재의 값. dp는 (N+1)*(N+1) / board는 N*N 따라서, i-1,j-1 이 현재값을 가르키는 것이다.
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + board[i - 1][j - 1]



for k in range(len(lst_point)):
    x1,y1,x2,y2 = lst_point[k]
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])
