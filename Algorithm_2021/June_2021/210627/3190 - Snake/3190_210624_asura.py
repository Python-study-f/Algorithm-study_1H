d = [(0,1),(1,0),(0,-1),(-1,0)]

N = int(input())
K = int(input())

board = [[0] * (N + 1) for _ in range(N + 1)] # N+1 크기의 Board 만들기.

for _ in range(K):
    x, y = map(int, input().split())
    board[x][y] = 1  # 사과 체크

L = int(input())
oper = []

for _ in range(L):
    a, b = map(str, input().split())
    oper.append([a, b])

snake = [(1, 1)]  # 뱀 몸둥아리 체크
d = [(0,1),(1,0),(0,-1),(-1,0)]
dic = 0
time = 0
x, y = 1, 1

while True:
    time += 1
    x, y = x + d[dic][0], y + d[dic][1]

    if 1 <= x <= N and 1 <= y <= N:
        snake.append((x, y))

        for i in snake[:-1]: # 자기 자신과 부딪힌 경우
            if (x,y) == i:
                print(time)
                exit()

        if board[x][y] == 0: # 그냥 통로일 경우 꼬리 삭제
            snake.pop(0)

        if board[x][y] == 1: # 사과일 경우 그냥 진행
            board[x][y] = 0

    else: # 벽 부딪힌 경우
        print(time)
        break

    if oper and time==int(oper[0][0]):

        if oper[0][1]=='D': # 오른쪽 90
            dic= dic+1 if dic<3 else 0
            oper.pop(0)
        elif oper[0][1]=='L': # 왼쪽 90
            dic = dic - 1 if dic > 0 else 3
            oper.pop(0)
