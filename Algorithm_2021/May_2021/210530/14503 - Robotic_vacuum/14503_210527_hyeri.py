N, M = map(int, input().split())
r, c, d = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
turn = {0: 3, 1: 0, 2: 1, 3: 2}

visit[r][c] = True
ans = 1
while True:
    for i in range(4):
        d = turn[d]
        tr = r + dr[d]
        tc = c + dc[d]
        if 0 <= tr < N and 0 <= tc < M and mp[tr][tc] == 0 and not visit[tr][tc]:
            visit[tr][tc] = True
            r = tr
            c = tc
            ans += 1
            break
    else:   # 4방향 다 갈 곳이 없을때
        tr = r - dr[d]
        tc = c - dc[d]
        if 0 <= tr < N and 0 <= tc < M and mp[tr][tc] == 0:
            r = tr
            c = tc
        else:
            break

print(ans)




