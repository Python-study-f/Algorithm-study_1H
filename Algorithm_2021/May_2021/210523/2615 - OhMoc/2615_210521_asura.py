'''

전제 1.
-> DFS 구현없이 그냥 brute-force 해도되지 않을까? 최단경로가 아니고 어차피 일정방향 + 일정횟수니깐 dfs말고 완탐으로
-> 6목은 이긴 것이 아니니 꼭 체크
-> 방향성은 for ( for )) 방향성은 아래, 아래오른쪽대각선, 오른쪽, 왼쪽 아래 대각선 총 4가지 탐색

'''

def check_omock(x,y,val):
    for dic in dictional:
        cnt = 1
        double_count = 0
        nx, ny = x + dic[0], y + dic[1]

        for _ in range(4):
            if 0 <= nx <19 and 0<= ny < 19:
                if board[nx][ny] == val:
                    cnt += 1
                    nx += dic[0]
                    ny += dic[1]

        if cnt == 5:
            if not 0 <= x-dic[0] <19 or not 0<= y-dic[1] < 19:
                double_count += 1
            else:
                if board[x-dic[0]][y-dic[1]] != val:
                    double_count += 1

            if not 0 <= nx <19 or not 0<= ny < 19:
                double_count += 1
            else:
                if board[nx][ny] != val:
                    double_count += 1

        if double_count == 2:
            return True
    return False



board = [[] for _ in range(19)]
ans = []
dictional = [(1,0),(1,1),(0,1),(-1,1)] # 아래, 아래오른쪽대각선, 오른쪽, 왼쪽 아래 대각선

for i in range(19):
    board[i] = list(map(int,input().split()))


for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            if check_omock(i,j,board[i][j]):
                ans.append((board[i][j],i+1,j+1))

if len(ans) == 0:
    print("0")
else:
    print(ans[0][0])
    print(ans[0][1],ans[0][2])
