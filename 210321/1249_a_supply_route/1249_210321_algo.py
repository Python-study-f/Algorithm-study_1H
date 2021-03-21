from collections import deque


T = int(input())

for num in range(1, T + 1):
    N = int(input())

    INF = float("inf")
    temp = [list(map(int, input())) for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited = [[INF] * N for _ in range(N)]
    visited[0][0] = 0  

    # L,R,U,D
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if temp[nx][ny] + visited[x][y] < visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + temp[nx][ny]
                q.append((nx, ny))

    answer = visited[N - 1][N - 1]
    print('#{} {}'.format(num, answer))
