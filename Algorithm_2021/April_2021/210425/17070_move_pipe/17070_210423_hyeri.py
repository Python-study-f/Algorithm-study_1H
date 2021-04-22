N = int(input())
mp = [[*map(int, input().split())] for _ in range(N)]
ret = 0


# 가로 0 세로 1 대각선 2
def dfs(x, y, d):
    global ret
    if x == N - 1 and y == N - 1:
        ret += 1
        return
    if d == 0:
        if y + 1 < N and mp[x][y + 1] == 0:
            dfs(x, y + 1, 0)
            if x + 1 < N and mp[x + 1][y] == 0 and mp[x + 1][y + 1] == 0:
                dfs(x + 1, y + 1, 2)
    elif d == 1:
        if x + 1 < N and mp[x + 1][y] == 0:
            dfs(x + 1, y, 1)
            if y + 1 < N and mp[x][y + 1] == 0 and mp[x + 1][y + 1] == 0:
                dfs(x + 1, y + 1, 2)
    else:
        if y + 1 < N and mp[x][y + 1] == 0:
            dfs(x, y + 1, 0)
        if x + 1 < N and mp[x + 1][y] == 0:
            dfs(x + 1, y, 1)
        if x + 1 < N and y + 1 < N and mp[x + 1][y] == 0 and mp[x][y + 1] == 0 and mp[x + 1][y + 1] == 0:
            dfs(x + 1, y + 1, 2)
    return


dfs(0, 1, 0)
print(ret)
