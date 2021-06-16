from itertools import product

dx,dy = [-1,0,1,0], [0,1,0,-1]
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
order = [None, [1], [1,3], [0,1], [0,1,3], [0,1,2,3]]

def draw(x,y,o,p):
    global temp
    sight = list(map(lambda x:(x+p)%4, order[o]))
    for i in sight:
        xi,yi = x+dx[i], y+dy[i]

        while (0<=xi<n and 0<=yi<m) and arr[xi][yi] < 6:
            if tvis[xi][yi] == 0:
                tvis[xi][yi] = 1
                temp -= 1
            xi+=dx[i]
            yi+=dy[i]

camera = {}
cnt = 0
total = 0
vis = [[0]*m for _ in range(n)]
for x in range(n):
    for y in range(m):
        if 0 < arr[x][y] < 6:
            cnt += 1
            camera[cnt] = (x,y,arr[x][y])
            vis[x][y] = 1
        elif arr[x][y] == 0:
            total += 1
        
condition = [0,1,2,3]
perms = list(product(condition, repeat=cnt))

ans = 1e9

for perm in perms:
    temp = total
    tvis = [i[:] for i in vis]
    cameras = list(camera.values())
    for i in range(len(perm)):
        x,y,o = cameras[i]
        p = perm[i]
        draw(x,y,o,p)
    ans = min(ans,temp)

print(ans)