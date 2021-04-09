T = int(input())
P = 0
result = 0
ln = 0
visit = []


def dfs(st, cnt):
    global result, P, ln
    if cnt == P:
        if result < int(st):
            result = int(st)
        return
    for i in range(ln):
        for j in range(i + 1, ln):
            temp = st[:i] + st[j] + st[i+1:j] + st[i] + st[j + 1:]
            if not visit[cnt][int(temp)]:
                visit[cnt][int(temp)] = True
                dfs(temp, cnt + 1)


for test_case in range(1, T + 1):
    S, P = input().split()
    P = int(P)
    ln = len(S)
    result = 0
    visit = [[False] * pow(10, ln) for _ in range(P + 1)]
    visit[0][int(S)] = True
    dfs(S, 0)
    print("#{} {}".format(test_case, result))
