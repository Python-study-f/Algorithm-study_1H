A, B = map(int, input().split())
N, M = map(int, input().split())
dir = {"N": 0, "W": 1, "S": 2, "E": 3}

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

arr = []
mp = [[0]*(A+1) for _ in range(B+1)]
for i in range(N):
    x, y, d = input().split()
    dd = dir[d]
    x = int(x)
    y = int(y)
    arr.append([dd, [B-y+1, x]])
    mp[B-y+1][x] = i + 1


for i in range(M):
    r, f, cnt = input().split()
    r = int(r)
    cnt = int(cnt)
    x = arr[r-1][1][0]
    y = arr[r-1][1][1]
    if f == 'L':
        for k in range(cnt):
            arr[r-1][0] = arr[r-1][0]+1
            if arr[r-1][0] == 4:
                arr[r-1][0] = 0

    elif f == 'R':
        for k in range(cnt%4):
            arr[r-1][0] = arr[r-1][0] - 1
            if arr[r-1][0] < 0:
                arr[r-1][0] = 3
    elif f == 'F':
        for k in range(1, cnt+1):
            tx = x + dx[arr[r-1][0]]
            ty = y + dy[arr[r-1][0]]
            if tx <= 0 or tx > B or ty <= 0 or ty > A:
                print("Robot "+str(r)+" crashes into the wall")
                exit()
            if mp[tx][ty] != 0:
                print("Robot "+str(r)+" crashes into robot "+str(mp[tx][ty]))
                exit()
            mp[tx][ty] = r
            mp[x][y] = 0
            x = tx
            y = ty
            arr[r-1][1][0] = tx
            arr[r-1][1][1] = ty

print("OK")
