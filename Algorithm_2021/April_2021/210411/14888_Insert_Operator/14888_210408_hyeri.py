mi, ma = int(1e9), -int(1e9)

n = int(input())
num = list(map(int,input().split()))
op = list(map(int,input().split()))


def dfs(idx, cnt):
    if idx == n:
        global ma, mi
        ma, mi = max(ma, cnt), min(mi, cnt)
        return

    else:
        for i in range(4):
            if op[i] > 0:
                op[i] -= 1
                if i == 0:
                    dfs(idx + 1, cnt + num[idx])
                elif i == 1:
                    dfs(idx + 1, cnt - num[idx])
                elif i == 2:
                    dfs(idx + 1, int(cnt * num[idx]))
                else:
                    dfs(idx + 1, int(cnt / num[idx]))
                op[i] += 1

    return


dfs(1, num[0])
print(ma)
print(mi)

