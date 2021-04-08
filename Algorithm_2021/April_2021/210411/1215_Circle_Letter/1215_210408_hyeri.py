T = 10

for test_case in range(1, T + 1):
    len = int(input())
    tmap = [list(input()) for _ in range(8)]
    ret = 0

    # 가로 검사
    for i in range(8):
        for j in range(9-len):
            chk = True
            s = j
            e = j + len - 1
            for k in range(int(len/2)):
                if tmap[i][s+k] != tmap[i][e-k]:
                    chk = False
                    break
            if chk:
                ret += 1

    # 세로 검사
    for j in range(8):
        for i in range(9-len):
            chk = True
            s = i
            e = i + len - 1
            for k in range(int(len/2)):
                if tmap[s+k][j] != tmap[e-k][j]:
                    chk = False
                    break
            if chk:
                ret += 1
    print("#{} {}".format(test_case, ret))
