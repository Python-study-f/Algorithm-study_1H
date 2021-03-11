
# print(answer)

import collections

dx = [-1, 1, 2]

def bfs(cur):
    visited = [0] * 100001
    time = 0
    q = collections.deque()
    q.append((cur, time))
    visited[cur] = 1
    nexttime=0
    while q:
        cur, time = q.popleft()
        if cur == k:
           break
        for i in range(len(dx)):
            if i == 2:
                next_cur = cur * dx[i]
            else:
                next_cur = cur + dx[i]
            if 0 > next_cur or next_cur > 100001:
                continue
            if visited[next_cur] == 0:
                visited[next_cur] = 1
                if next_cur == cur * 2:
                    q.appendleft((next_cur, time))
                else:
                    nexttime=time+1
                    visited[next_cur] = 1
                    q.append((next_cur, nexttime))

    return time


n, k = map(int, input().split())
answer = bfs(n)
print(answer)


