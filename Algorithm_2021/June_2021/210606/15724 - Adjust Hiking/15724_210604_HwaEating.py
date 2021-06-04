from collections import deque

dx,dy = [-1,0,1,0], [0,1,0,-1]

def dfs(x,y,k,cnt=1):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        xi,yi = x+dx[i], y+dy[i]
        if 0<=xi<n and 0<=yi<n and vis[xi][yi] == 0:
            vis[xi][yi] = 1
            if arr[xi][yi] < arr[x][y]:
                dfs(xi,yi,k,cnt+1)
            elif arr[xi][yi]-k < arr[x][y]:
                temp = arr[xi][yi]
                arr[xi][yi] = arr[x][y] - 1
                dfs(xi,yi,0,cnt+1)
                arr[xi][yi] = temp
            vis[xi][yi] = 0

for T in range(1,int(input())+1):
    n,k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    ans = 1
    mHeight = 0
    peaks = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] > mHeight:
                peaks = [(i,j)]
                mHeight = arr[i][j]
            elif arr[i][j] == mHeight:
                peaks.append((i,j))
    
    queue = deque(peaks)
    vis = [[0]*n for _ in range(n)]
    while queue:
        x,y = queue.popleft()
        vis[x][y] = 1
        dfs(x,y,k)
        vis[x][y] = 0
    print(f'#{T} {ans}')
    