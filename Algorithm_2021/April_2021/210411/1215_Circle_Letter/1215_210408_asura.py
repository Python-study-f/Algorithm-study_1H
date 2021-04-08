def ispalindromic(s):
    return s == s[::-1]

def right_rotate(graph):
    n = len(graph)

    ret = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            ret[c][n-1-r] = graph[r][c]

    return ret

ans = []

for T in range(10):
    cnt = 0
    # 설정 + 초기값 세팅 #
    N = int(input())
    data = [[] for _ in range(8)]

    for i in range(8):
        data[i] = str(input())

    # 가로 체크 #
    for i in range(8):
        for j in range(9-N):
            if ispalindromic(data[i][j:j+N]):
                cnt += 1

    # 세로 체크 #
    graph = right_rotate(data)
    for i in range(8):
        for j in range(9-N):
            if ispalindromic(graph[i][j:j+N]):
                cnt += 1
    ans.append(cnt)

for k in range(1,11):
    print('#{0} {1}'.format(k,ans[k-1]))


