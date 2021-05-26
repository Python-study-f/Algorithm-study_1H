import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y,lim):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            xi,yi = x+dx[i], y+dy[i]
            if 0<=xi<n and 0<=yi<n and vis[xi][yi] == 0 and arr[xi][yi] > lim:
                vis[xi][yi] = 1
                queue.append((xi,yi))

dx,dy = [-1,0,1,0], [0,1,0,-1]
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
_max = -1e9
_min = 1e9
_ans = 1
for i in range(n):
    for j in range(n):
        _max = max(_max, arr[i][j])
        _min = min(_min, arr[i][j])

for lim in range(_min, _max):
    _cnt = 0
    vis = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > lim and vis[i][j] == 0:
                bfs(i,j,lim)
                _cnt += 1
    _ans = max(_ans, _cnt)

print(_ans)