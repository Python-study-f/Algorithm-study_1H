from collections import deque
import sys

input=sys.stdin.readline

graph=[]
n=int(input())

dx=[-1,1,0,0]
dy=[0,0,-1,1]
height=0
max_size=0

for _ in range(n):
    h=list(map(int,input().split()))
    for i in range(len(h)):
        height = max(h[i],height)
    graph.append(h)

check=[[[False]*n for _ in range(n)]for _ in range(height)]
def bfs(x,y,z):
    queue=deque()
    queue.append([x,y])
    check[z][x][y]=True
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and check[z][nx][ny]==False and graph[nx][ny]>z:
                queue.append([nx,ny])
                check[z][nx][ny]=True

for z in range(0,height):
    cnt=0
    for i in range(n):
        for j in range(n):
            if graph[i][j]>z and check[z][i][j]==False:
                bfs(i,j,z)
                cnt+=1
        max_size=max(max_size,cnt)

print(max_size)
