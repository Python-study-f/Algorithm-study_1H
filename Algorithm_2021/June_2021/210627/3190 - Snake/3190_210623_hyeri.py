from collections import deque

N = int(input())
K = int(input())
mp = [[0] * (N + 1) for _ in range(N + 1)]
apple = []
snake = []
ldir = {1: 4, 2: 1, 3: 2, 4: 3}
ddir = {1: 2, 2: 3, 3: 4, 4: 1}

for _ in range(K):
    a, b = map(int, input().split())
    apple.append([a, b])
    mp[a][b] = 1

L = int(input())
for _ in range(L):
    a, b = input().split()
    a = int(a)
    snake.append([a, b])

mp[1][1] = 2

t = 1
idx = 0
dq = deque()
dq.append([1, 1])
direc = 1
x = 1
y = 1
dx = [0, 0, 1, 0, -1]
dy = [0, 1, 0, -1, 0]
while True:
    tx = x + dx[direc]
    ty = y + dy[direc]
    if tx > N or ty > N or tx < 1 or ty < 1 or mp[tx][ty] == 2:
        break
    elif mp[tx][ty] == 1:
        x = tx
        y = ty
        mp[x][y] = 2
        dq.append([x, y])
    else:
        x = tx
        y = ty
        mp[x][y] = 2
        dq.append([x, y])
        dn= dq.popleft()
        mp[dn[0]][dn[1]] = 0

    if idx < len(snake) and snake[idx][0] == t:
        if snake[idx][1] == "L":
            direc = ldir[direc]
        elif snake[idx][1] == "D":
            direc = ddir[direc]
        idx += 1
    t += 1

print(t)
