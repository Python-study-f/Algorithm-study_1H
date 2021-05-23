Dy= [-1,0,1,0]
Dx= [0,1,0,-1]
for _ in range(int(input())):
    s= input()
    dir=0
    y,x=0,0
    minx=0
    maxx=0
    miny=0
    maxy=0
    for el in s:
        if el=='L':
            dir= (dir+4-1)%4
        elif el=='R':
            dir=(dir+1)%4
        elif el=='F':
            y+=Dy[dir]
            x+=Dx[dir]
        else:
            y+=Dy[(dir+2)%4]
            x+=Dx[(dir+2)%4]
        minx= min(minx,x)
        maxx= max(maxx,x)
        miny=min(miny,y)
        maxy= max(maxy,y)
    print((maxx-minx)*(maxy-miny))


