import sys; input= lambda:sys.stdin.readline().rstrip(); 
sys.setrecursionlimit(50000)
n, m= map(int, input().split())
mp= [[*map(int, input().split())] for _ in range(n)]

Dy= [0,0,1,-1]
Dx= [1,-1,0,0]
out= [[False]*m for _ in range(n)]
def outside(y, x):
    
    for dy, dx in zip(Dy, Dx):
        ny= y+dy
        nx= x+dx
        if 0<=nx and nx<m and 0<=ny and ny<n:
            if not mp[ny][nx] and not out[ny][nx]:
                out[ny][nx]=True
                mp[ny][nx]=-1
                outside(ny, nx)


candi= set()
for c in range(m):
    if not mp[0][c]: # outside found
        candi.add((0,c))
        mp[0][c]=-1
        out[0][c]=True
        outside(0, c)

for c in range(m):
    if not mp[n-1][c]: # outside found
        candi.add((n-1,c))
        mp[n-1][c]=-1
        out[n-1][c]=True
        outside(m-1, c)

for r in range(n):
    if not mp[r][0]: # outside found
        candi.add((r,0))
        mp[r][0]=-1
        out[r][0]=True
        outside(r, 0)

for r in range(n):
    if not mp[r][m-1]: # outside found
        candi.add((r,m-1))
        mp[r][m-1]=-1
        out[r][m-1]=True
        outside(r, m-1)


chk=[[False]*m for _ in range(n)]
def melt(y, x):
    #print(y, x)
    for dy, dx in zip(Dy, Dx):
        ny= y+dy
        nx= x+dx
        if 0<=nx and nx<m and 0<=ny and ny<n:
            if mp[ny][nx]==1:
                cnt=0
                for sy, sx in zip(Dy, Dx):
                    cy= ny+sy
                    cx= nx+sx
                    
                    if 0<=cx and cx<m and 0<=cy and cy<n:
                        if out[cy][cx]:
                            cnt+=1
                if cnt>=2:
                    nxt.append((ny, nx))
                    chk[ny][nx]=True
            elif mp[ny][nx]==-1 and not chk[ny][nx]:
                chk[ny][nx]=True
                melt(ny, nx)

t=0
nxt=[]
candi=list(candi)
print(candi)
[print(*el) for el in mp]
while candi:
    t+=1
    nxt=[]
    for y, x in candi:
        melt(y, x)



    for y, x in nxt:
        chk[y][x]=False
        mp[y][x]=-1
        out[y][x]=True
        outside(y, x)
    nxt=list(nxt)
    candi=nxt[:]
    print()
    [print(*el) for el in mp]
    print()
    [print(*el) for el in out]

print(t-1)


'''
8 9
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 1 1 0
0 1 0 1 1 1 0 1 0
0 1 0 0 1 0 0 1 0
0 1 0 1 1 1 0 1 0
0 1 1 0 0 0 1 1 0
0 0 0 0 0 0 0 0 0


8 9
0 0 0 0 0 0 0 0 0
0 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 0
0 1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0

4 4
1 0 1 0
1 1 0 1
1 0 1 1
0 1 1 0
'''