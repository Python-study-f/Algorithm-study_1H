'''
from collections import deque
dx = [0, 1]
dy = [1, 0]
visisted = []
dist=[]
q = deque()
temp=[]

def bfs(x, y,n,m):
    global visited
    visited[x][y] = 1
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if temp[nx][ny]==0 and visited[nx][ny]==0:
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                    bfs(nx, ny,n,m)
    return dist[n-1][m-1]

def solution(m, n, puddles):
    answer = 0
    global temp
    global visited
    global dist
    temp = [[0 for j in range(m)] for i in range(n)]
    visited = [[0 for j in range(m)] for i in range(n)]
    dist = [[0] * m for _ in range(n)]
    tt=100000000
    for i, j in puddles:
        temp[i - 1][j - 1] = -1
    for i in range(n):
        for j in range(m):
            answer=bfs(i,j,n,m)
            tt=min(answer,tt)
    #answer=bfs(0, 0)
    return tt-1
'''

def solution(m,n,puddles):
    temp=[[0] *(m+1) for i in range(n+1)]
    temp[1][1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1:
                continue
            if [j,i] in puddles:
                temp[i][j]=0
            else:
                temp[i][j]=temp[i-1][j]+temp[i][j-1]
                
            #print(temp)
    return temp[n][m]%1000000007
