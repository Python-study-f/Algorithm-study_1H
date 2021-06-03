from collections import deque

N = int(input())
dq = deque()
tower = list(map(int, input().split()))
for i in range(N):
    rt = 0
    if not dq:
        dq.append([tower[i], i])
    else:
        while dq and dq[-1][0] < tower[i]:
            dq.pop()
        if dq:
            rt = dq[-1][1] + 1
        dq.append([tower[i], i])
    print(rt, end=' ')





