near = [[-1,0], [0,1], [1,0], [0,-1]]
rcw = [[0,-1], [1,0], [0,1], [-1,0]]


def debug():
    for i in bd:
        print(i)
    print(f'robot = {robot}')
    print(f'success = {success}')

# def make_p(d,i):
#     if d == 0:
        

def go_clean():
    while True:
        # debug()
        mach_one()
        if mach_two() == 1:
            break


def mach_one():
    global success
    x,y,d = robot
    if bd[x][y] == 0:
        bd[x][y] = -1
        success += 1


def mach_two():
    global robot
    x,y,d = robot
    p = rcw.index(near[d])
    for i in range(1,5):
        a,b = rcw[(i+p)%4]
        xi, yi = a+x, b+y
        if 0 <= xi < n and 0 <= yi < m and bd[xi][yi] == 0:
            robot = [xi,yi,(4+d-i)%4]
            return 0
    a,b = near[(d+2)%4]
    xi, yi = a+x, b+y
    if 0 <= xi < n and 0 <= yi < m and bd[xi][yi] != 1:
        robot = [xi,yi,d]
        mach_two()
    else:
        return 1


n,m = map(int, input().split())
r,c,d = map(int,input().split())
robot = [r,c,d]
bd = [list(map(int,input().split())) for i in range(n)]
success = 0

go_clean()
print(success)

