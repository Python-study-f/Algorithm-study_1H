import sys
sys.setrecursionlimit(100000)

N = int(input())
mp = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

mx = 0
for i in range(N):
    for j in range(N):
        mx = max(mx, mp[i][j])
result = 0

visit = []
def dfs(x, y, n, K):
    for d in range(4):
        tx = x + dx[d]
        ty = y + dy[d]
        if tx < 0 or ty < 0 or tx >= N or ty >= N:
            continue
        if visit[tx][ty] == 0 and mp[tx][ty] > K:
            visit[tx][ty] = n
            dfs(tx, ty, n, K)

# 단지번호 
for k in range(mx + 1):
    num = 1
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0 and mp[i][j] > k:
                visit[i][j] = num
                dfs(i, j, num, k)
                num += 1
    num -= 1
    result = max(result, num)

print(result)
