from collections import deque

# 입력값 받기
T = int(input())

for i in range(1,T+1):
    N = int(input())

    # 초기화
    INF = int(1e9)
    data = [list(map(int,input())) for _ in range(N)]
    dq = deque()
    dq.append((0,0))
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0 # 시작점

    #L,R,U,D
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while dq:
        x,y = dq.popleft()

        for d in range(4): # L,R,U,D
            nx, ny = x + dx[d], y + dy[d]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if data[nx][ny] + dist[x][y] < dist[nx][ny]:
                dist[nx][ny] = dist[x][y] + data[nx][ny]
                dq.append((nx,ny))

    answer = dist[N-1][N-1]
    print('#{} {}'.format(i,answer))