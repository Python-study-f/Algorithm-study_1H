N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]

result = 0


def chk(x, y):
    global result
    n = 0
    # 가로검사
    for i in range(4):
        if y + i >= M:
            break
        n += mp[x][y + i]
        if i == 3:
            result = max(result, n)
        elif i == 2:
            if x + 1 < N:
                result = max(result, n + mp[x + 1][y])
                result = max(result, n + mp[x + 1][y + 1])
                result = max(result, n + mp[x + 1][y + 2])
            if x - 1 >= 0:
                result = max(result, n + mp[x - 1][y])
                result = max(result, n + mp[x - 1][y + 1])
                result = max(result, n + mp[x - 1][y + 2])
        elif i == 1:
            if x + 1 < N:
                result = max(result, n + mp[x + 1][y] + mp[x + 1][y + 1])
                if x - 1 >= 0:
                    result = max(result, n + mp[x + 1][y] + mp[x - 1][y + 1])
                    result = max(result, n + mp[x + 1][y + 1] + mp[x - 1][y])

                    result = max(result, n + mp[x + 1][y] + mp[x - 1][y])
                    result = max(result, n + mp[x + 1][y + 1] + mp[x - 1][y + 1])
                if y - 1 >= 0:
                    result = max(result, n + mp[x + 1][y] + mp[x + 1][y - 1])
                if y + 2 < M:
                    result = max(result, n + mp[x + 1][y + 1] + mp[x + 1][y + 2])
            if x - 2 >= 0:
                result = max(result, n + mp[x - 1][y] + mp[x - 2][y])
                result = max(result, n + mp[x - 1][y + 1] + mp[x - 2][y + 1])
            if x + 2 < N:
                result = max(result, n + mp[x + 1][y] + mp[x + 2][y])
                result = max(result, n + mp[x + 1][y + 1] + mp[x + 2][y + 1])
        if i == 0:
            if x + 3 < N:
                result = max(result, n + mp[x + 1][y] + mp[x + 2][y] + mp[x + 3][y])
    return


for a in range(N):
    for b in range(M):
        chk(a, b)

print(result)
