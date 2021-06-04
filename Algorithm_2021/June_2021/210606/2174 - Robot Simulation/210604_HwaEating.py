dx,dy = [1,0,-1,0], [0,1,0,-1]

col, row = map(int,input().split())
n,m = map(int,input().split())
arr = [[0]*(col+1) for _ in range(row+1)]
robots = {}
for num in range(1,n+1):
    y,x,p = input().split()
    x,y = map(int,[x,y])
    if p == 'N':
        p = 0
    elif p == 'E':
        p = 1
    elif p == 'S':
        p = 2
    elif p == 'W':
        p = 3
    robots[num] = [x,y,p]
    arr[x][y] = num

for _ in range(m):
    num, order, times = input().split()
    num,times = map(int,[num,times])
    x,y,p = robots[num]
    if order == 'L':
        p = (p-times)%4
    elif order == 'R':
        p = (p+times)%4
    else:
        arr[x][y] = 0
        xi,yi = dx[p],dy[p]
        for _ in range(times):
            x += xi
            y += yi
            if 0<x<=row and 0<y<=col:
                if arr[x][y]:
                    print(f'Robot {num} crashes into robot {arr[x][y]}')
                    exit()
            else:
                print(f'Robot {num} crashes into the wall')
                exit()
        arr[x][y] = num
    robots[num] = [x,y,p]

print('OK')

