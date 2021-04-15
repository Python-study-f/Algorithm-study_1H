from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
mp = [[*map(int, input().split())] for _ in range(N)]
visit = [[0] * M for _ in range(N)]


def dfs(x, y, n):
    for d in range(4):
        ttx = x + dx[d]
        tty = y + dy[d]
        if ttx < 0 or ttx >= N or tty < 0 or tty >= M:
            continue
        if mp[ttx][tty] == 0 and visit[ttx][tty] == 0:
            visit[ttx][tty] = n
            dfs(ttx, tty, n)


def dfs2(x, y):
    for d in range(4):
        ttx = x + dx[d]
        tty = y + dy[d]
        if ttx < 0 or ttx >= N or tty < 0 or tty >= M:
            continue
        if mp[ttx][tty] == 0 and visit[ttx][tty] != 2:
            visit[ttx][tty] = 2
            dfs2(ttx, tty)


def check():
    for c in range(N):
        print(*mp[c])
    print("\n")

    for c in range(N):
        print(*visit[c])
    print("\n")


dq = deque()
dqq = deque()
ss = 0

for i in range(N):
    for j in range(M):
        if mp[i][j] == 1:
            dq.append([i, j])
            visit[i][j] = 1
            ss += 1

# 얼음이 없는 연결 된 공간 표시
num = 2
visit[0][0] = num
dfs(0, 0, num)
num += 1

# 3 부터는 연결되지 않은 내부 공간 (단지 번호 붙이기)
for i in range(N):
    for j in range(M):
        if visit[i][j] == 0:
            visit[i][j] = num
            dfs(i, j, num)
            num += 1

sec = 0
while True:
    if ss <= 0:
        break
    dqq.clear()

    #check()
    # 2면이 공기층인 얼음
    for k in range(len(dq)):
        nx = dq[k][0]
        ny = dq[k][1]
        if mp[nx][ny] == 0:
            continue
        cnt = 0
        for i in range(4):
            tx = nx + dx[i]
            ty = ny + dy[i]
            if tx < 0 or tx >= N or ty < 0 or ty >= M:
                continue
            if visit[tx][ty] == 2:
                cnt += 1
        if cnt >= 2:
            dqq.append([nx, ny])


    # 치즈 제거 및 맵 체인지
    ss -= len(dqq)
    for k in range(len(dqq)):
        nx = dqq[k][0]
        ny = dqq[k][1]
        mp[nx][ny] = 0
        visit[nx][ny] = 2
        dfs2(nx, ny)

    sec += 1

print(sec)
