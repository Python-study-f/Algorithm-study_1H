import sys; sys.setrecursionlimit(100000)
answer=1e9
def solution(b):
    global answer
    n= len(b[0])
    Dy= [0,0,1,-1]
    Dx= [1,-1,0,0]
    dp= [[[1e9]*n for _ in range(n)] for _ in range(4)]
    for i in range(4):
        dp[i][n-1][n-1]=0
    answer= 1e9
    def topdown(y, x, cost, d):
        print(y, x, cost, d)
        if y+x==0:
            global answer
            answer= min(answer, cost)
            return

        for dir, (dy, dx) in enumerate(zip(Dy, Dx)):
            ny= y+dy
            nx= x+dx
            if 0<=nx and nx<n and 0<=ny and ny<n :
                if b[ny][nx]==0:
                    if d==dir or d==-1:
                        if cost+100<dp[dir][ny][nx]:
                            dp[dir][ny][nx]=cost+100
                            topdown(ny, nx, cost+100, dir)
                    else:
                        if cost+600<dp[dir][ny][nx]:
                            dp[dir][ny][nx]=cost+600
                            topdown(ny, nx, cost+600,dir)

    topdown(n-1, n-1, 0,-1)

    return answer


print(solution(	[[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
