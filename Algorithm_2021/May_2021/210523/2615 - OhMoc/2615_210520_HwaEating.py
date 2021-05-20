arr = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, 1]
dy = [1, 0, 1, -1]

for x in range(19):
    for y in range(19):
        if arr[x][y]:
            for i in range(4):
                xi,yi = x+dx[i], y+dy[i]
                cnt = 1
                while 0<=xi<19 and 0<=yi<19 and arr[xi][yi] == arr[x][y]:
                    cnt += 1
                    xi += dx[i]
                    yi += dy[i]
                
                if cnt == 5:
                    xi,yi = x-dx[i], y-dy[i]
                    if 0<=xi<19 and 0<=yi<19 and arr[x][y] == arr[xi][yi]:
                        continue
                    else:
                        print(arr[x][y])
                        print(x+1, y+1)
                        exit()

print(0)