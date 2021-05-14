R, C, T = map(int, input().split())
mp = [[*map(int, input().split())] for _ in range(R)]
tmp = [[0] * C for _ in range(R)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cl = [3, 0, 2, 1]
cr = [2, 0, 3, 1]

air = []
for i in range(R):
    for j in range(C):
        tmp[i][j] = mp[i][j]
        if mp[i][j] == -1:
            air.append([i, j])

for _ in range(T):
  
   # 미세먼지 확산
    for i in range(R):
        for j in range(C):
            if mp[i][j] > 0:
                dust = 0
                for m in range(4):
                    ti = i + dx[m]
                    tj = j + dy[m]
                    if ti < 0 or tj < 0 or ti >= R or tj >= C or mp[ti][tj] == -1:
                        continue
                    else:
                        tmp[ti][tj] += int(mp[i][j] / 5)
                        dust += int(mp[i][j] / 5)
                tmp[i][j] -= dust

    # 윗쪽순환
    x, y = air[0]
    d = 0
    while True:
        tx = x + dx[cl[d]]
        ty = y + dy[cl[d]]
        if tx < 0 or ty < 0 or tx >= R or ty >= C or tx > air[0][0]:
            d += 1
            if d == 4:
                d = 0
        tx = x + dx[cl[d]]
        ty = y + dy[cl[d]]

        if mp[tx][ty] == -1:
            break
        if mp[x][y] != -1:
            tmp[x][y] = tmp[tx][ty]
        tmp[tx][ty] = 0
        x = tx
        y = ty

    # 아랫쪽 순환
    x, y = air[1]
    d = 0
    while True:
        tx = x + dx[cr[d]]
        ty = y + dy[cr[d]]
        if tx < 0 or ty < 0 or tx >= R or ty >= C or tx < air[1][0]:
            d += 1
            if d == 4:
                d = 0
        tx = x + dx[cr[d]]
        ty = y + dy[cr[d]]
        if mp[tx][ty] == -1:
            break
        if mp[x][y] != -1:
            tmp[x][y] = tmp[tx][ty]
        tmp[tx][ty] = 0
        x = tx
        y = ty

    for i in range(R):
        for j in range(C):
            mp[i][j] = tmp[i][j]

answer = 0
for i in range(R):
    for j in range(C):
        answer += mp[i][j]

print(answer + 2)

# 구현, 시뮬레이션, 삼성 기출?
