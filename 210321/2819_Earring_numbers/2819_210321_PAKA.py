dx = ( 1, -1, 0, 0)
dy = ( 0, 0, 1, -1)

def DFS(y, x, s):
    if len(s) > 6:
        rst.add(s)
        return;
    for se in range(4):
        nx = x + dx[se]
        ny = y + dy[se]
        if 0 <= nx < 4 and 0 <= ny < 4:
            DFS(ny, nx, s+field[ny][nx])

for i in range(int(input())):
    #init
    field = []
    rst = set()
    rst.clear()
    for j in range(4):
        field.append(input().split())

    for r in range(4):
        for c in range(4):
            DFS(r, c, field[r][c])
  
    #print(field)
    print('#{} {}'.format(i+1, len(rst)))