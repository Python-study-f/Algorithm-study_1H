dx,dy = [-1,0,1,0],[0,1,0,-1]

for T in range(int(input())):
    left = 0
    right = 0
    top = 0
    bottom = 0
    order = input()
    x,y,p = 0,0,0
    for o in order:
        if o == 'F':
            x += dx[p]
            y += dy[p]
        elif o == 'B':
            x -= dx[p]
            y -= dy[p]
        elif o == 'L':
            p -= 1
            p %= 4
        elif o == 'R':
            p += 1
            p %= 4
        left = min(left,y)
        right = max(right,y)
        top = min(top,x)
        bottom = max(bottom,x)

    print((right-left) * (bottom-top))
