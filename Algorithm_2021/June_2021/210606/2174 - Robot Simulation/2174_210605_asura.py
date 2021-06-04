dx = [1, 0, -1, 0]  # N E S W
dy = [0, 1, 0, -1]
turn = {'N': 0, 'E': 1, 'S': 2, 'W': 3}


A, B = map(int, input().split())
N, M = map(int, input().split())
board = [[0] * A for _ in range(B)]
robots = [[0,0,0]]


for i in range(N):
    x,y,dic = input().split()
    x,y = int(x)-1, int(y)-1 # 값 보정
    board[y][x] = i+1
    d = turn[dic]
    robots.append([d,y,x]) # 로봇 배열 입력

for _ in range(M):
    robot, cmd, cnt = input().split()
    robot, cnt = int(robot),int(cnt) #변수 타입 변경

    for _ in range(cnt):
        if cmd == 'L':
            robots[robot][0] = (robots[robot][0] - 1) % 4 # index 보정
        elif cmd == 'R':
            robots[robot][0] = (robots[robot][0] + 1) % 4
        else: # F 진행

            index = robots[robot][0]
            x,y = robots[robot][1],robots[robot][2]
            nx,ny = robots[robot][1] + dx[index], robots[robot][2] + dy[index]

            if not 0 <= nx < B or not 0 <= ny < A:
                print("Robot {} crashes into the wall".format(robot))
                exit()

            if board[nx][ny] != 0:
                print("Robot {} crashes into robot {}".format(robot, board[nx][ny]))
                exit()

            board[x][y] = 0
            board[nx][ny] = robot # 로봇 이동 시, 좌표변경
            robots[robot][1] = nx
            robots[robot][2] = ny

print("OK")

'''
5 4
2 2
1 1 E
5 4 W
1 F 7
2 F 7
[[0, 0, 0], [1, 0, 0], [3, 3, 4]]
'''

