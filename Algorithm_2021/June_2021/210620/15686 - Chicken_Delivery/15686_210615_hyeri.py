INF = 987654321

N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
h = []
c = []

result = INF
for i in range(N):
    for j in range(N):
        if mp[i][j] == 1:
            h.append([i, j])
        elif mp[i][j] == 2:
            c.append([i, j])

hsiz = len(h)
csiz = len(c)


def chk():
    global result, hsiz, csiz
    mini = 0
    for hi in range(hsiz):
        hx = h[hi][0]
        hy = h[hi][1]
        num = INF
        for cj in range(0, csiz):
            cx = c[cj][0]
            cy = c[cj][1]
            if mp[cx][cy] == 2:
                a = abs(hx - cx) + abs(hy - cy)
                num = min(num, a)
        mini += num
    result = min(result, mini)


def dfs(cnt, total, idx):
    if cnt >= total:
        chk()
        return
    for r in range(idx + 1, csiz):
        x = c[r][0]
        y = c[r][1]
        mp[x][y] = 0
        dfs(cnt + 1, total, r)
        mp[x][y] = 2


dfs(0, csiz - M, -1)

print(result)
