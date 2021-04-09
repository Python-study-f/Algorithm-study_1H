
'''
dirs = "ULURRDLLU"
visited = [[[[[False]*10] for _ in range(10)] for _ in range(10)] for _ in range(10)]
# 간선리스트로 간선을 표현해보면 어떨까? 그렇게 함으로 4차원 리스트 생성
# 어차피 공간이 제한적이므로 시간초과는 안나올 거 같음.

x,y = 5,5
tot_len = 0
#초기값 설정

d= {}
d['L'] = (-1,0)
d['R'] = (1,0)
d['U'] = (0,1)
d['D'] = (0,-1)

for dr in dirs:
    a,b = d.get(dr)
    nx , ny = x + a , y + b

    if 0<=nx<=10 and 0<=ny<=10:
        if not visited[nx][ny][x][y]: # 출발점x, 출발점y , 도착점x, 도착점y
            visited[nx][ny][x][y] = True
            visited[x][y][nx][ny] = True
            tot_len += 1

        x, y = nx, ny

print(tot_len)

https://minnnne.tistory.com/41
아니 이 친구는 되는데 왜 나는 안되는거징? 아시는분 알려주세욘 ㅠㅠ..
'''


def solution(dirs):
    visited = set()
    # 간선리스트로 간선을 표현해보면 어떨까? 그렇게 함으로 4차원 리스트 생성
    # 어차피 공간이 제한적이므로 시간초과는 안나올 거 같음.

    x,y = 5,5
    tot_len = 0
    #초기값 설정

    d= {}
    d['L'] = (-1,0)
    d['R'] = (1,0)
    d['U'] = (0,1)
    d['D'] = (0,-1)

    for dr in dirs:
        a,b = d.get(dr)
        nx , ny = x + a , y + b

        if 0<=nx<=10 and 0<=ny<=10:
            if (x,y,nx,ny) not in visited:
                visited.add((x,y,nx,ny))
                visited.add((nx,ny,x,y))
                tot_len += 1

            x, y = nx, ny

    return tot_len