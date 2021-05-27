dx = [-1,0,1,0] # 북,동,남,서 초기 방향 설정
dy = [0,1,0,-1]
turn = { 0 : 3, 1 : 0, 2 : 1, 3 : 2} #해쉬를 이용해 for문 사용없이 direction 찾기

def check_condition(a,b):
    global N,M

    if 0 <= a < N and 0 <= b < M:
        return True
    return False

N,M = map(int,input().split())
x,y,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

tot_cnt = 1
board[x][y] = 2 # 방문처리. 처음에 무조건 0값 준다고 나옴

while True:
    check = False
    for _ in range(4):
        d = turn[d]
        nx, ny = x + dx[d], y + dy[d]

        if check_condition(nx,ny):
            if board[nx][ny] == 0:
                tot_cnt += 1
                board[nx][ny] = 2 # 방문처리
                x , y = nx, ny
                check = True
                break

    if not check:
        nx,ny = x - dx[d], y - dy[d]
        if check_condition(x,y):
            if board[nx][ny] == 2: # 청소한 칸일 경우 후진
                x,y = nx, ny
            if board[nx][ny] == 1:
                print(tot_cnt)
                break
        else:
            print(tot_cnt)
            break

# for i in board: # 출력부분
#     print(i)
