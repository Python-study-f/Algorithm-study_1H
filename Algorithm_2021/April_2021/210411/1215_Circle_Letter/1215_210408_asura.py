def ispalindromic(s):
    return s == s[::-1]
ans = []

for T in range(10):
    cnt = 0
    # 설정 + 초기값 세팅 #
    N = int(input())
    data = [[] for _ in range(8)]

    for i in range(8):
        data[i] = str(input())
    rotate_data = list(map(list, zip(*data)))

    # 가로 체크 #
    for i in range(8):
        for j in range(9 - N):
            if ispalindromic(data[i][j:j + N]):
                cnt += 1

    # 세로 체크 #
    for i in range(8):
        for j in range(9 - N):
            if ispalindromic(rotate_data[i][j:j + N]):
                cnt += 1
    ans.append(cnt)

for k in range(1, 11):
    print('#{0} {1}'.format(k, ans[k - 1]))