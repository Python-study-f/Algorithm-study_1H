from collections import deque

def solution(board):
    answer = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    N = len(board)
    x = 0
    y = 0
    d = 0
    visit = [[[False] * N for _ in range(N)] for _ in range(2)]

    def checkN(cx, cy):
        if 0 <= cx < N and 0 <= cy < N and board[cx][cy] == 0:
            return True
        else:
            return False

    dq = deque()  # 0 : 가로, 1 : 세로
    dq.append([d, x, y])
    visit[d][x][y] = True
    while dq:
        qs = len(dq)
        print(dq)
        for _ in range(qs):
            nq = dq.popleft()
            if (nq[1] == N - 1 and nq[2] == N - 1) or (nq[1] + dx[nq[0]] == N - 1 and nq[2] + dy[nq[0]] == N - 1):
                return answer
            for i in range(4):  # 4방향 이동
                tx = nq[1] + dx[i]
                ty = nq[2] + dy[i]
                if checkN(tx, ty) and checkN(tx + dx[nq[0]], ty + dy[nq[0]]):
                    if not visit[nq[0]][tx][ty]:
                        visit[nq[0]][tx][ty] = True
                        dq.append([nq[0], tx, ty])
                    # 회전
                    if nq[0] == 0:  # 가로축 회전 -> 세로
                        if i == 3:
                            if not visit[1][tx][ty]:
                                visit[1][tx][ty] = True
                                dq.append([1, tx, ty])
                            if not visit[1][tx][ty+1]:
                                visit[1][tx][ty+1] = True
                                dq.append([1, tx, ty+1])
                        elif i == 1:
                            if not visit[1][nq[1]][nq[2]]:
                                visit[1][nq[1]][nq[2]] = True
                                dq.append([1, nq[1], nq[2]])
                            if not visit[1][nq[1]][nq[2]+1]:
                                visit[1][nq[1]][nq[2]+1] = True
                                dq.append([1, nq[1], nq[2]+1])
                    if nq[0] == 1:  # 세로축 회전 -> 가로
                        if i == 0:
                            if not visit[0][nq[1]][nq[2]]:
                                visit[0][nq[1]][nq[2]] = True
                                dq.append([0, nq[1], nq[2]])
                            if not visit[0][nq[1]+1][nq[2]]:
                                visit[0][nq[1]+1][nq[2]] = True
                                dq.append([0, nq[1]+1, nq[2]])
                        elif i == 2:
                            if not visit[0][tx][ty]:
                                visit[0][tx][ty] = True
                                dq.append([0, tx, ty])
                            if not visit[0][tx+1][ty]:
                                visit[0][tx+1][ty] = True
                                dq.append([0, tx+1, ty])
        answer += 1
    return 0

  # 상대축으로 회전하는걸 고려하지 않아서 틀렸었음
  # 축 회전 좌표 규칙성을 찾아서 코드 줄이는 법 찾기 
