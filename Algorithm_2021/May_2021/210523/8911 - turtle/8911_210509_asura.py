N = int(input())

ans = []
dic = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(N):
    x,y = 0, 0
    x_max,x_min,y_max,y_min = 0,0,0,0
    index = 0
    lst = list(str(input()))
    SET = set()
    SET.add((0, 0))


    for c in lst:
        if index % 4 == 0:
            index = 0

        nx,ny = dic[index]
        if c == "L":
            index -= 1
        elif c == "R":
            index += 1
        elif c == "F":
            x,y = x+nx, y+ny
        else:  # Back
            x,y = x-nx, y-ny

        SET.add((x, y))  # 좌표까지 구했으면 이제 사각형 구해야한다

    for s in SET:
        a, b = s
        x_max = max(x_max, a)
        x_min = min(x_min, a)
        y_max = max(y_max, b)
        y_min = min(y_min, b)
    col = abs(x_max - x_min)
    row = abs(y_max - y_min)

    ans.append(col * row)

for i in range(len(ans)):
    print(ans[i])