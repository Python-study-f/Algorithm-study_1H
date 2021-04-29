N = int(input())
ret = 0
mp = [[*map(int, input().split())] for _ in range(N)]
v1 = []
v2 = []
d1 = [0] * 21
d2 = [0] * 21
ret = 0
for i in range(N):
    for j in range(N):
        if mp[i][j] == 1:
            if i % 2 == 0:
                if j % 2 == 0:
                    v1.append([i, j])
                else:
                    v2.append([i, j])
            else:
                if j % 2 == 1:
                    v1.append([i, j])
                else:
                    v2.append([i, j])


def dfs1(idx, cnt):
    global ret, N
    if ret < cnt:
        ret = cnt
    if idx == len(v1):
        return
    x = v1[idx][0]
    y = v1[idx][1]
    if d1[x + y] == 0 and d2[N + (y - x)] == 0:
        d1[y + x] = d2[N + (y - x)] = 1
        dfs1(idx + 1, cnt + 1)
        d1[y + x] = d2[N + (y - x)] = 0
    dfs1(idx + 1, cnt)


def dfs2(idx, cnt):
    global ret, N
    if ret < cnt:
        ret = cnt
    if idx == len(v2):
        return
    x = v2[idx][0]
    y = v2[idx][1]
    if d1[x + y] == 0 and d2[N + (y - x)] == 0:
        d1[y + x] = d2[N + (y - x)] = 1
        dfs2(idx + 1, cnt + 1)
        d1[y + x] = d2[N + (y - x)] = 0
    dfs2(idx + 1, cnt)


dfs1(0, 0)
total = ret
ret = 0
dfs2(0, 0)
total += ret
print(total)
