from collections import deque
Dy= [0,0,1,-1]
Dx= [1,-1,0,0]
storage=[]
chk=[]
mat=[]
matchk=[]
ln=deque()
n=0
def dfs(y, x):
    #print(y,x)
    global n
    y1, y2= y, y
    x1, x2= x, x
    for dy, dx in zip(Dy, Dx):
        ny= y+dy
        nx= x+dx
        if 0<=ny<n and 0<=nx<n:
            if storage[ny][nx] and not chk[ny][nx]:
                chk[ny][nx]=True
                ny1, ny2, nx1, nx2= dfs(ny, nx)
                y1= min(y1, ny1)
                y2= max(y2, ny2)
                x1= min(x1, nx1)
                x2= max(x2, nx2)
    return y1, y2, x1, x2

def matlink(r, c, m):
    if len(ln)==m:
        return True
    flag=False
    for i in range(m):
        if not matchk[i] and mat[i][0]==c:
            matchk[i]=True
            ln.append(mat[i])
            flag= flag or matlink(r, mat[i][1],m)
            if flag: break
            ln.pop()
            matchk[i]=False
            
        if not matchk[i] and mat[i][1]==r:
            matchk[i]=True
            ln.appendleft(mat[i])
            flag=flag or matlink(mat[i][0], c,m)
            if flag: break
            ln.popleft()
            matchk[i]=False
            
    if not flag:
        return False
    else:
        return True


for t in range(int(input())):
    n= int(input())
    storage=[ [*map(int, input().split())] for _ in range(n)]
    if n==1:
        print(f'#{t+1} 0')
        continue
    chk= [[False]*n for _ in range(n)]
    mat=[]
    for i in range(n):
        for j in range(n):
            if storage[i][j] and not chk[i][j]:
                chk[i][j]=True
                y1, y2, x1, x2= dfs(i,j)
                mat.append((y2-y1+1, x2-x1+1))
    m= len(mat)
    matchk=[False]*m
    matchk[0]=True
    ln.clear()
    ln.append(mat[0])
    matlink(mat[0][0], mat[0][1],m)
    mat= list(ln)
    dp= [[1e9]*m for _ in range(m)]
    for i in range(m):
        for j in range(m-i):
            if not i:
                dp[j][j+i]=0 # 1. 자기자신 하나는 연산없지
            elif i==1:
                dp[j][j+i]= mat[j][0]*mat[j][1]*mat[j+i][1]
            else:
                for k in range(j,j+i):
                    dp[j][j+i]= min(dp[j][k]+ mat[j][0]*mat[k+1][0]*mat[j+i][1]+dp[k+1][j+i], dp[j][j+i]) # 2. 두 묶음 잇는 연산 생각 잘못함
    #[print(*el) for el in dp]
    print(f'#{t+1} {dp[0][m-1]}')

'''
1
9
1 1 3 2 0 0 0 0 0
0 0 0 0 0 0 0 0 0
1 1 3 2 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 1
0 1 0 0 0 0 0 0 1
0 1 0 0 0 0 0 0 1
0 1 0 0 0 0 0 0 1

1
1
'''