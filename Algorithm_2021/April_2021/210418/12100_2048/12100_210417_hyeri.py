from collections import deque

N = int(input())
mp = [[*map(int, input().split())] for _ in range(N)]


def check(tmp):
    for i in range(N):
        print(*tmp[i])
    print()


def bfs():
    dq = deque()
    dq.append(mp)
    ans = 0
    for c in range(6):
        for qs in range(len(dq)):
            v = dq.popleft()
            #print("time:{}".format(c))
            #check(v)

            for i in range(N):
                for j in range(N):
                    ans = max(ans, v[i][j])

            # up
            vv = [[0] * N for _ in range(N)]
            for j in range(N):
                q = deque()
                for i in range(N):
                    if v[i][j] != 0:
                        if len(q) > 0 and q[len(q) - 1] == v[i][j]:
                            q.pop()
                            q.append(v[i][j] * -2)
                        else:
                            q.append(v[i][j])
                for i in range(N):
                    if len(q) > 0:
                        vv[i][j] = abs(q.popleft())
                    else:
                        vv[i][j] = 0
            dq.append(vv)

            # down
            vv = [[0] * N for _ in range(N)]
            for j in range(N):
                q = deque()
                for i in range(N - 1, -1, -1):
                    if v[i][j] != 0:
                        if len(q) > 0 and q[len(q) - 1] == v[i][j]:
                            q.pop()
                            q.append(v[i][j] * -2)
                        else:
                            q.append(v[i][j])
                for i in range(N - 1, -1, -1):
                    if len(q) > 0:
                        vv[i][j] = abs(q.popleft())
                    else:
                        vv[i][j] = 0
            dq.append(vv)

            # right
            vv = [[0] * N for _ in range(N)]
            for i in range(N):
                q = deque()
                for j in range(N-1, -1, -1):
                    if v[i][j] != 0:
                        if len(q) > 0 and q[len(q) - 1] == v[i][j]:
                            q.pop()
                            q.append(v[i][j] * -2)
                        else:
                            q.append(v[i][j])
                for j in range(N-1, -1, -1):
                    if len(q) > 0:
                        vv[i][j] = abs(q.popleft())
                    else:
                        vv[i][j] = 0
            dq.append(vv)

            # left
            vv = [[0] * N for _ in range(N)]
            for i in range(N):
                q = deque()
                for j in range(N):
                    if v[i][j] != 0:
                        if len(q) > 0 and q[len(q) - 1] == v[i][j]:
                            q.pop()
                            q.append(v[i][j] * -2)
                        else:
                            q.append(v[i][j])
                for j in range(N):
                    if len(q) > 0:
                        vv[i][j] = abs(q.popleft())
                    else:
                        vv[i][j] = 0
            dq.append(vv)

    return ans

print(bfs())
