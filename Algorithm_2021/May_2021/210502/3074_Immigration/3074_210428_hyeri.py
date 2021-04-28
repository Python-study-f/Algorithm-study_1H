T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    mx = 0
    x = 0
    v = []
    for i in range(N):
        x = int(input())
        v.append(x)
        mx = max(mx, x)
    lef = 1
    rig = mx*M
    ret = rig
    while lef <= rig:
        mid = int((lef + rig) / 2)
        n = 0
        for i in range(N):
            n += int(mid / v[i])
        if n < M:
            lef = mid + 1
        else:
            rig = mid - 1
            ret = min(ret, mid)
    print("#{} {}".format(t, ret))

