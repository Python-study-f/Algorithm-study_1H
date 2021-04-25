
'''

0. board를 리스트로 만들자
1. X,Y 좌표로 생각해서 왼쪽 밑부터 오른쪽 위 방향으로
2. visited 함수 만들어서 4x4 블럭이 된다면 다 visit 했다고 표시
    # 만약 visited 가 True였다고 하면, ans -1 을 실행
3. 마지막으로 for문 반대로 돌리면서 visited[False] 나올 때까지 행으로 줄 내리기
4. 이 전체가 해당 되지 않을 때 까지 전체 돌린다.
'''

def check_visited(a,b,c,d): # 중복제거
    global ans

    if a:
        ans -= 1
    if b:
        ans -= 1
    if c:
        ans -= 1
    if d:
        ans -= 1

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
# Output = 15

ans = 0
flag = False # 전체 체크하는 것을 확인해주기 위한 flag
visited = [[False] * m for _ in range(n)]

for i in range(len(board)): # 문자열 -> 리스트
    tmp = board.pop(0)
    board.append([t for t in tmp])


while not flag: # 더이상 블록이 터지지 않는다면 flag = True

    for i in range(m): ## 전체 터질 폭탄들 체크
        for j in range(n):
            if 0<= i+1 < m and 0<= j+1 < n: # 인덱스 안넘어갔을 때만
                check = board[i][j] # 해당 board 값 확인

                if board[i+1][j] == check and board[i][j+1] == check and board[i+1][j+1] == check: # 4개의 블록이 같을 때
                        check_visited(visited[i][j],visited[i+1][j],visited[i][j+1],visited[i+1][j+1])
                        visited[i][j], visited[i+1][j], visited[i][j+1], visited[i+1][j+1] = True, True, True, True
                        ans += 4

    for i in range(m): # 폭탄 제거하기
        for j in range(n):
            if visited[i][j]:
                board[i][j] = "_"

    for i in range(m): ## 폭탄 내리기.. 수정중
        for j in range(n):


    flag = True

for i in range(len(board)):
    print(board[i])


