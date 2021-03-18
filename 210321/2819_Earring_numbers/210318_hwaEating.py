near = [[0,1],[1,0],[-1,0],[0,-1]]
def go(x,y,st):
    if len(st) == 7:
        vis[st] = 1
        return
    for dx, dy in near:
        xi = x+dx
        yi = y+dy
        if 0 <= xi < 4 and 0 <= yi < 4:
            go(xi,yi,st+bd[xi][yi])


for t in range(int(input())):
    bd = [list(input().split()) for i in range(4)]
    vis = {}
    for x in range(4):
        for y in range(4):
            go(x,y,bd[x][y])
    print('#{}'.format(t+1),len(vis))