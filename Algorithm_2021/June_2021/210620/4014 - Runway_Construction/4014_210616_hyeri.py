T = int(input())

for test_case in range(1, T+1):
    N, X = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(N)]
    num = 0

    # 가로검사
    for i in range(N):
        chk = True
        m = mp[i][0]
        n = 1
        j = 1
        while j < N:
            if abs(mp[i][j]-m) > 1:
                chk = False
                break
            elif mp[i][j] == m:
                n += 1
            elif mp[i][j] == m + 1:
                if n < X:
                    chk = False
                    break
                else:
                    n = 1
                    m += 1
            elif mp[i][j] == (m - 1):
                for x in range(1, X):
                    if (j + x) >= N:
                        chk = False
                        break
                    if mp[i][j+x] != (m-1):
                        chk = False
                        break
                if chk:
                    j = j + X - 1
                    n = 0
                    m = m - 1
                else:
                    break
            j += 1
        if chk:
            num += 1

    # 세로검사
    for j in range(N):
        chk = True
        m = mp[0][j]
        n = 1
        i = 1
        while i < N:
            if abs(mp[i][j]-m) > 1:
                chk = False
                break
            elif mp[i][j] == m:
                n += 1
            elif mp[i][j] == (m + 1):
                if n < X:
                    chk = False
                    break
                else:
                    n = 1
                    m += 1
            elif mp[i][j] == (m - 1):
                for x in range(1, X):
                    if (i + x) >= N:
                        chk = False
                        break
                    if mp[i+x][j] != (m - 1):
                        chk = False
                        break
                if chk:
                    i = i + X - 1
                    n = 0
                    m = m - 1
                else:
                    break
            i += 1
        if chk:
            num += 1

    print("#{} {}".format(test_case, num))
