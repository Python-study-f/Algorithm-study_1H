from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for test_case in range(1, T + 1):
    # init
    n = int(input())
    maps = [[0 for col in range(n)] for row in range(n)]
    field = [[float('inf') for col in range(n)] for row in range(n)]
    field[0][0] = 0

    # 구멍 입력
    for i in range(n):
        tmpStr = input()
        for j in range(n):
            maps[i][j] = int(tmpStr[j])

    # bfs -> 선택이유: 댓글보고
    queue = deque()
    queue.append((0,0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=n or ny < 0 or ny >= n:
                continue

            # 결국 field[-1][-1]에 도달시 가장 작은값이 통과
            if field[x][y] + maps[nx][ny] < field[nx][ny]:
                field[nx][ny] = field[x][y] + maps[nx][ny]
                queue.append((nx, ny))

    print('#{} {}'.format(test_case, field[-1][-1]))