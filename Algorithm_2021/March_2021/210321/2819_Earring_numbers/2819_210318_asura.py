from collections import deque

def bfs(pos,cnt,my_str):
    x, y = pos

    if cnt == 7:
        lst_set.add(my_str)
        return

    for d in range(4): # L,R,U,D
        nx, ny = x + dx[d], y + dy[d]

        if nx >= 0 and ny >= 0 and nx < 4 and ny < 4:

            dfs((nx,ny),cnt+1,my_str+str(data[nx][ny]))


# 입력값
T = int(input())
data = [list(map(int,input().split())) for _ in range(4)]

# 설정값
dx = [0,0,-1,1]
dy = [-1,1,0,0]
lst_set = set()
dq = deque()

for i in range(4):
    for j in range(4):
        bfs((i,j),0,'')

print(len(lst_set))
