from collections import deque

# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

def dfs(v):
    print(v, end= ' ')
    visited[v] = True                   # 노드 방문 기록 = True
    for i in graph[v]:                  
        if visited[i] == False:         
            dfs(i)                      # 재귀 질의 (더욱 깊이 들어간다.)

def bfs(v):
    queue = deque()                     # deque() 함수를 이용하여 queue 생성
    queue.append(v)                     # v 추가
    visited[v] = True                   # 노드 방문 기록 = True
    print(v, end=' ')                   # 출력
    while queue:                        # queue 동안
        v = queue.popleft()             # queue에 있는 맨 왼쪽 원소를 뺸다.
        for i in graph[v]:              # graph[v]를 for문 돌림 (인접 노드 모두 탐색)
            if visited[i] == False:
                queue.append(i)             # queue에 추가시킨다.
                visited[i] = True           # 노드 방문 기록 = True
                print(i, end=' ')           # 출력


n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]      # Empty Graph array

visited = [False] * (n + 1)             # 방문 횟수

for i in range(m):
    # 각 노드가 어떤 노드와 인접해있는지를 파악해주는 graph array
    x, y = map(int, input().split())
    graph[x].append(y)                  # x번째 인덱스 리스트에 y를 추가
    graph[y].append(x)                  # y번째 인덱스 리스트에 x를 추가

for i in graph:                         # 순서가 뒤집어 진 경우를 대비하여 sorting        
    i.sort()

dfs(v)
visited = [False] * (n + 1)
print()
bfs(v)