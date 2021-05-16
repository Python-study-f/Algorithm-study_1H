import sys; input= lambda:sys.stdin.readline().rstrip()
r, c, t= map(int, input().split())
mp= [[*map(int, input().split())] for _ in range(r)]
cleaner=[[0]*2 for _ in range(2)]
up=[]
down=[]

for i in range(r): # 문제 7: 세상에
    if mp[i][0]==-1:
        cleaner[0][0]=i # 문제 6: 여기가 문제
        cleaner[1][0]=i+1
        break

y, x= cleaner[0][0], 0

while x<c-1:
    x+=1
    up.append((y,x))
    
while 1<=y:
    y-=1
    up.append((y,x))
while 0<x: # 문제 3 여기까지 돌려야하네
    x-=1
    up.append((y,x))
while y<cleaner[0][0]-1:
    y+=1
    up.append((y,x))

y, x= cleaner[1][0], 0

while x<c-1:
    x+=1
    down.append((y,x))
while y<r-1:
    y+=1
    down.append((y,x))
while 0<x:
    x-=1
    down.append((y,x))
while cleaner[1][0]+1<y:
    y-=1
    down.append((y,x))
Dy=[0,0,1,-1]
Dx=[1,-1,0,0]

#print(up)
#print(down)
while t:
    t-=1
    dust=[]
    for i in range(r):
        for j in range(c):
            if mp[i][j]>0:
                dust.append((i,j,mp[i][j]))
    
    for y, x, dst in dust:
        cnt=0 # 문제 2: 이거 밖으로 빼놈
        for dy, dx in zip(Dy, Dx):
            ny=dy+y
            nx=dx+x
            if 0<=ny<r and 0<=nx<c:
                if mp[ny][nx]==-1:
                    continue
                cnt+=1
                mp[ny][nx]+=dst//5
        mp[y][x]= mp[y][x]-(dst//5)*cnt # 문제 1: 계산
    #[print(*el)  for el in mp]
    #print()
    ccw=[]
    ups=len(up)
    for y, x in up[:ups-1]:
        ccw.append(mp[y][x])
    mp[up[0][0]][up[0][1]]=0 # 문제 5: 얜 치워야함
    for idx,(y, x) in enumerate(up[1:]):  # 문제 4: 정화된대
        mp[y][x]=ccw[idx]

    cw=[]
    downs=len(down)
    for y, x in down[:downs-1]:
        cw.append(mp[y][x])
    mp[down[0][0]][down[0][1]]=0
    for idx,(y, x) in enumerate(down[1:]):
        mp[y][x]=cw[idx]
    #[print(*el)  for el in mp]
    
    #print()
    
ans=0
for i in range(r):
    for j in range(c):
        if mp[i][j]>0:
            ans+=mp[i][j]
print(ans)


'''
6 8 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
-1 0 0 0 0 0 0 0
-1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

8 8 2
3 0 0 0 0 0 0 0
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0

7 7 1
0 0 0 0 0 0 0
0 0 0 0 0 0 0
-1 0 0 0 0 0 0
-1 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 10


6 6 1
0 0 0 0 0 0
0 0 0 0 0 0
-1 1 0 0 0 0
-1 0 0 0 0 0
1 0 0 0 0 0
0 0 0 0 0 0
'''