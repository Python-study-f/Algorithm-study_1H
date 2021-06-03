from collections import deque

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    dq = deque()
    mp = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mp[i][j] == 1:
                dq.append([i, j])

    def cal(n):
        if  n <= 0:
            return 0
        else:
            return n * n + (n - 1) * (n - 1)

    mx = 0
    arr = []
    for i in range(N):
        for j in range(N):
            for m in range(len(dq)):
                nx = dq[m][0]
                ny = dq[m][1]
                arr.append(abs(nx-i) + abs(ny-j) + 1)

            arr.sort()
            for m in range(len(arr)):
                if cal(arr[m]) <= ((m+1)*M):
                    mx = max(mx, m+1)
            arr.clear()

    print("#{} {}".format(test_case, mx))
