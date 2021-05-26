import sys; input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001)
n= int(input())
mp=[[*map(int, input().split())] for _ in range(n)]
Dy= [0,0,1,-1]
Dx= [1,-1,0,0]
ans=1
for floor in range(1,101):
    chk=[[False]*n for _ in range(n)]
    def dfs(y,x):
        global floor
        for dy, dx in zip(Dy, Dx):
            ny=y+dy
            nx=x+dx
            if 0<=ny<n and 0<=nx<n:
                if mp[ny][nx]>floor and not chk[ny][nx]:
                    chk[ny][nx]=True
                    dfs(ny,nx)
    cnt=0
    for i in range(n):
        for j in range(n):
            if not chk[i][j] and mp[i][j]>floor:
                cnt+=1
                chk[i][j]=True
                dfs(i,j)
    ans=max(ans,cnt)

print(ans)