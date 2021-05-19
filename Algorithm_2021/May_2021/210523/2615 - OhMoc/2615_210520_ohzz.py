# 오목 2615 백준

arr = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, 1]
dy = [1, 0, 1, -1]


def chekingIndex(x, y):
    if x < 19 and x >= 0 and y < 19 and y >= 0:
        return True
    return False


def checkOmok():
    for j in range(19):
        for i in range(19):
            if arr[j][i] > 0:
                for k in range(4):
                    x, y = i, j
                    cnt = 1
                    while chekingIndex(x + dx[k], y + dy[k]) and (
                        arr[j][i] == arr[y + dy[k]][x + dx[k]]
                    ):
                        x, y = x + dx[k], y + dy[k]
                        cnt += 1

                    if cnt == 5:
                        if chekingIndex(i - dx[k], j - dy[k]) and (
                            arr[j][i] == arr[j - dy[k]][i - dx[k]]
                        ):
                            break
                        else:
                            return arr[j][i], i + 1, j + 1
    return 0, 0, 0


ans = checkOmok()

if ans[0] == 0:
    print(0)
else:
    print(ans[0])
    print(ans[2], ans[1])
