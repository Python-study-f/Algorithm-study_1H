from collections import deque

# 입력값
N, K = map(int,input().split())

# 초기값 생성
LIM = 100000
dq = deque()
visited = [False] * 100001
dist = [-1] * 100001


# 초기값 설정
dq.append(N)
dist[N] = 0
visited[N] = True

while dq:
    now = dq.popleft() # 우선순위라고 생각하면 됨.

    if now == K: #now와 K가 같으면 break로 while문 탈출
        break

    if 0 <= now * 2 <= LIM and visited[now*2] == False:
        dq.appendleft(now*2) # pop이 아닌 popleft로 한 이유는 위에서 popleft로 함으로 순서를 임의로 제공
        visited[now*2] = True
        dist[now*2] = dist[now] # 만약, 순간이동에 시간이 있었으면, 이 부분에서 컨트롤해주면 된다.

    if 0 <= now+1 <= LIM and visited[now+1] == False:
        dq.append(now+1)
        visited[now+1] = True
        dist[now+1] = dist[now] + 1

    if 0 <= now-1 <= LIM and visited[now-1] == False:
        dq.append(now-1)
        visited[now-1] = True
        dist[now-1] = dist[now] +1

print(dist[K])

'''
1. 문제보자마자 DP, DFS , BFS 셋 중 하나라고 판단 -> 1) 가장 빠른 / X-1 , X+1 , X*2 / DFS로 하기엔 모든 리프를 건드릴 필요가 없어보였음
2. DP로 풀기에는 범위에서나 더 문제를 잘게 쪼갤 수 없어 보여서 BFS로 접근.
3. 가장 기본적인 BFS 문제였던 거 같음.
'''