# 톱니바퀴(2) 15662 백준
import collections

T = int(input())

arr = [collections.deque(input()) for _ in range(T)]
ans = 0


def rotate(r, index):
    if r == -1:
        tmp = arr[index].popleft()
        arr[index].append(tmp)
    else:
        tmp = arr[index].pop()
        arr[index].insert(0, tmp)


k = int(input())
for _ in range(k):
    n, r = map(int, input().split())
    cnt = 0
    tmpr = r
    tmp = arr[n - 1][2]
    lt = arr[n - 1][6]
    rotate(r, n - 1)
    for i in range(n - 2, -1, -1):
        rt = arr[i][2]

        if lt != rt:
            if r < 0:
                r = 1
            else:
                r = -1
            lt = arr[i][6]
            rotate(r, i)
        else:
            break

    rt = tmp
    r = tmpr
    for j in range(n, T):
        lt = arr[j][6]

        if lt != rt:
            if r < 0:
                r = 1
            else:
                r = -1
            rt = arr[j][2]
            rotate(r, j)
        else:
            break


for s in range(T):
    if arr[s][0] == "1":
        ans += 1

print(ans)
