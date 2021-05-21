T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for test_case in range(T):
    move = input()
    x = mx = y = my = nx = ny = 0
    d = 0

    for c in move:
        if c == 'F':
            x += dx[d]
            y += dy[d]
        elif c == 'B':
            x -= dx[d]
            y -= dy[d]
        elif c == 'L':
            d -= 1
        elif c == 'R':
            d += 1

        if d < 0:
            d = 3
        if d == 4:
            d = 0

        mx = max(mx, x)
        nx = min(nx, x)
        my = max(my, y)
        ny = min(ny, y)


    print(str((mx-nx)*(my-ny)))
