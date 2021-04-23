'''
문제 출제 실수 ^-^... 이렇게 더러운 문제일 줄은 몰랐어요 헤헤..
이번주 문제 누가 출제했어!!!
'''

N = int(input())
data = [[] for _ in range(N)]
ans = 0

for i in range(N):
    data[i] = list(map(int,input().split()))


# cur = 1 가로, 2 세로 3 대각선
def dfs(x,y,shape):
    global ans

    if x == N-1 and y == N-1: # 마지막 인덱스 도착
        ans += 1
        return

    else:
        if shape == 1: # 가로 진출일 때
            if x <= N-1 and y+1 <=N-1 and data[x][y+1] == 0:
                dfs(x, y+1,1) # 가로로 진출하기

            if x + 1 <= N - 1 and y + 1 <= N - 1 and data[x + 1][y + 1] == 0 and data[x+1][y] == 0 and data[x][y+1] == 0:
                dfs(x+1, y+1,3) # 대각선으로 진출

        elif shape == 2: # 세로 진출일 때
            if x+1 <= N-1 and y <=N-1 and data[x+1][y] == 0:
                dfs(x+1, y, 2) # 세로 진출

            if x + 1 <= N - 1 and y + 1 <= N - 1 and data[x + 1][y + 1] == 0 and data[x+1][y] == 0 and data[x][y+1] == 0:
                dfs(x+1,y+1,3) #대각선 진출

        elif shape == 3: # 대각 선 진출 일 때
            if x <= N - 1 and y + 1 <= N - 1 and data[x][y + 1] == 0:
                dfs(x, y + 1, 1)  # 가로로 진출하기

            if x+1 <= N-1 and y <=N-1 and data[x+1][y] == 0:
                dfs(x+1, y, 2) # 세로 진출

            if x + 1 <= N - 1 and y + 1 <= N - 1 and data[x + 1][y + 1] == 0 and data[x + 1][y] == 0 and data[x][
                y + 1] == 0:
                dfs(x + 1, y + 1, 3)  # 대각선으로 진출


dfs(0,1,1)
print(ans)