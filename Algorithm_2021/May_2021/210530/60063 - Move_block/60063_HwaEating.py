from collections import deque
dx,dy = [-1,0,1,0], [0,1,0,-1]
def solution(board):
    n = len(board)
    answer = 0
    vis = [[[1e9]*2 for _ in range(n)] for _ in range(n)]
    vis[0][0][0] = 0
    queue = deque()
    queue.append((0,0,0))
    cnt = 0
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x,y,p = queue.popleft()
            for i in range(4): # 이동
                xi,yi = x+dx[i], y+dy[i]
                if 0<=xi<n and 0<=yi<n:
                    if p == 0 and yi+1<n and board[xi][yi] == 0 and board[xi][yi+1] == 0 and vis[xi][yi][p] > cnt:
                        vis[xi][yi][p] = cnt
                        queue.append((xi,yi,p))
                    elif p == 1 and xi+1<n and board[xi][yi] == 0 and board[xi+1][yi] == 0 and vis[xi][yi][p] > cnt:
                        vis[xi][yi][p] = cnt
                        queue.append((xi,yi,p))
            if p == 0: # 회전 가로
                # 위로 가는거
                if 0<=x-1 and y+1<n and board[x-1][y] == 0 and board[x-1][y+1] == 0:
                    if vis[x-1][y][1] > cnt:
                        vis[x-1][y][1] = cnt
                        queue.append((x-1,y,1))
                    if vis[x-1][y+1][1] > cnt:
                        vis[x-1][y+1][1] = cnt
                        queue.append((x-1,y+1,1))
                # 아래로 가는거
                if x+1<n and y+1<n and board[x+1][y+1] == 0 and board[x+1][y] == 0:
                    if vis[x][y][1] > cnt:
                        vis[x][y][1] = cnt
                        queue.append((x,y,1))
                    if vis[x][y+1][1] > cnt:
                        vis[x][y+1][1] = cnt
                        queue.append((x,y+1,1))
            else: # 세로
                # 왼쪽으로 가는거
                if x+1<n and 0<=y-1 and board[x][y-1] == 0 and board[x+1][y-1] == 0:
                    if vis[x][y-1][0] > cnt:
                        vis[x][y-1][0] = cnt
                        queue.append((x,y-1,0))
                    if vis[x+1][y-1][0] > cnt:
                        vis[x+1][y-1][0] = cnt
                        queue.append((x+1,y-1,0))
                # 오른쪽으로 가는거
                if x+1<n and y+1<n and board[x][y+1] == 0 and board[x+1][y+1] == 0:
                    if vis[x][y][0] > cnt:
                        vis[x][y][0] = cnt
                        queue.append((x,y,0))
                    if vis[x+1][y][0] > cnt:
                        vis[x+1][y][0] = cnt
                        queue.append((x+1,y,0))
                        
    return min(vis[n-1][n-2][0], vis[n-2][n-1][1])