import sys; input= lambda:sys.stdin.readline().rstrip()
n= int(input())
board= [[*map(int, input().split())] for _ in range(n)]
candi=[[] for _ in range(2*n-1)]
for i in range(n): 
    for j in range(n):
        if board[i][j]:
            board[i][j]=0
        else:
            board[i][j]=-1

for i in range(n):
    y, x= 0,i
    if not board[y][x]:
        candi[i].append((y,x))
    while 0<x: 
        y+=1
        x-=1
        if not board[y][x]:
            candi[i].append((y,x))

for j in range(1,n):
    y, x= j, n-1
    if not board[y][x]:
        candi[n+j-1].append((y,x))
    while y<n-1: # 음 기울기 미리 해결: 시초해결1
        y+=1
        x-=1
        if not board[y][x]:
            candi[n+j-1].append((y,x))

ans=-1
def do(i, cnt):

    global ans
    ans= max(ans, cnt)
    if i==2*n-1:
        return
    flag=False
    for y, x in candi[i]:
        if board[y][x]==0:
            flag=True
            board[y][x]=1
            p_ry, p_rx= y, x
            while p_ry<n-1 and p_rx<n-1:# 양 기울기 해결
                p_ry+=1
                p_rx+=1
                if board[p_ry][p_rx]!=-1:
                    board[p_ry][p_rx]+=1
                
            do(i+1, cnt+1)
            board[y][x]=0
            e_ry, e_rx= y, x
            while e_ry<n-1 and e_rx<n-1:
                e_ry+=1
                e_rx+=1
                if board[e_ry][e_rx]!=-1:
                    board[e_ry][e_rx]-=1
    if not flag: # 비숍 못 놀 때만 패스시키기: 시초해결2
        do(i+1, cnt)
do(0,0)

print(ans)
