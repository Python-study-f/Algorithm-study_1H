# 파이프 옮기기 1 17070

n = int(input())

# 0 가로, 1 대각선, 2 세로


def dfs(x, y, pos):
    global res
    if x == n - 1 and y == n - 1:
        res += 1
        return
    else:
        if pos == 0 or pos == 1:
            if y + 1 < n:
                if wall[x][y + 1] == 0:
                    dfs(x, y + 1, 0)
        if pos == 1 or pos == 2:
            if x + 1 < n:
                if wall[x + 1][y] == 0:
                    dfs(x + 1, y, 2)
        if pos == 0 or pos == 1 or pos == 2:
            if x + 1 < n and y + 1 < n:
                if wall[x + 1][y] == 0 and wall[x + 1][y + 1] == 0 and wall[x][y + 1] == 0:
                    dfs(x + 1, y + 1, 1)


wall = [list(map(int, input().split())) for _ in range(n)]
res = 0
dfs(0, 1, 0)
print(res)
