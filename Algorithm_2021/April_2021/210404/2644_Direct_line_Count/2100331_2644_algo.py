from collections import deque

n = int(input())
x, y = map(int, input().split())  # x가 부모, y가 자식
m = int(input())
ans = -1  # 정답 마이너스 -1로 초기화
temp = [[] for i in range(n + 1)]
visit = [0] * (n + 1)  # 방문 버텍스 생성
# 인접 리스트로 만드는 방법.
dist = [0 for i in range(n + 1)]

visit = [0 for i in range(n + 1)]
def bfs(start):
    q = deque()
    q.append(start)
    
    visit[start] = 1
    while q:
        nx = q.popleft()
        for i in temp[nx]:
            if visit[i] == 0:
                visit[i] = 1
                dist[i] = dist[nx] + 1 # 촌수 계산
                q.append(i)


for i in range(m):
    a, b = map(int, input().split())
    temp[a].append(b)
    temp[b].append(a)
bfs(x)
if dist[y] == 0:
    print(-1)
else:
    print(dist[y])
