n = int(input())
numblist=[]
nums=0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
temp = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
cnt = 1
def dfs(x,y,c):

    visited[x][y]=1
    global nums
    if temp[x][y] ==1:
        nums +=1
    for i in range(4):
        nx =x+dx[i]
        ny =y+dy[i]
        if 0<=nx <n and 0<=ny <n:
            if visited[nx][ny]==0 and temp[nx][ny]==1:
                dfs(nx,ny,c)

def make():
    global nums
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j, cnt)
                numblist.append(nums)
                nums = 0



def ans():
    print(len(numblist))
    numblist.sort()
    for i in numblist:
        print(i)

if __name__ == '__main__':
    make()
    ans()
