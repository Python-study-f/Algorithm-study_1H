for test_case in range(1, T + 1):
    S = str(input())
    for i in range(2, 30):
        tmp = S[0:i]
        chk = True
        for j in range(i, 30-i, i):
            tmp2 = S[j:j+i]
            if tmp != tmp2:
                chk = False
                break
        if chk:
            break
    print("#{} {}".format(test_case, len(tmp)))
