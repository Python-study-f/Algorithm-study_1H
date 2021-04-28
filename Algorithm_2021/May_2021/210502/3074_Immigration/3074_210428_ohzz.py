# 입국심사 3074 SW Expert

T = int(input())

for c in range(T):
    n, m = map(int, input().split())

    time = []
    for i in range(n):
        time.append(int(input()))
    lt = min(time)
    rt = max(time) * m
    ans = 0
    while lt <= rt:
        tmp = 0
        mid = (lt + rt) // 2
        for k in time:
            tmp += mid // k
            if tmp >= m:
                break
        if tmp >= m:
            ans = mid
            rt = mid - 1
        else:
            lt = mid + 1
    print(f"#{c + 1} {ans}")
