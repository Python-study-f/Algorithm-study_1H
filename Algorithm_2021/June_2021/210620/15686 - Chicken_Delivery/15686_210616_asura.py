from itertools import combinations

N,M = map(int,input().split())
board = [[] for _ in range(N)]

for i in range(N):
    board[i] = list(map(int,input().split()))

house = []
chicken = []
ans = int(1e9)

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i,j)) # 집 정보 기록
        if board[i][j] == 2:
            chicken.append((i,j)) # 치킨 집 정보 기록


minv = int(1e9)
for ch in combinations(chicken,M): # Combination으로 조합 다 만들어서
    sumv = 0

    for home in house: # 집과
        sumv += min([abs(home[0] - i[0]) + abs(home[1] - i[1]) for i in ch]) # combination의 모든 거리 체크


        if minv <= sumv:
            break

    if sumv < minv:
        minv = sumv

print(minv)