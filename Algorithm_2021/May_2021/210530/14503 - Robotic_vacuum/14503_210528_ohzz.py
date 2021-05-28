# 로봇 청소기 14503 백준

n, m = map(int, input().split())

r, c, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn(d):
    if d == 0:
        return 3
    if d == 1:
        return 0
    if d == 2:
        return 1
    if d == 3:
        return 2


def checkIndex(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False


board = [list(map(int, input().split())) for _ in range(n)]


def clean(x, y, d, ans):
    board[x][y] = 2
    while True:
        for _ in range(4):
            d = turn(d)
            xx = x + dx[d]
            yy = y + dy[d]

            if checkIndex(xx, yy) and board[xx][yy] == 0:
                board[xx][yy] = 2
                ans += 1
                x, y = xx, yy
                break
        else:
            xx = x - dx[d]
            yy = y - dy[d]

            if checkIndex(xx, yy) and board[xx][yy] == 2:
                x, y = xx, yy
            else:
                break
    return ans


res = clean(r, c, d, 1)
print(res)
