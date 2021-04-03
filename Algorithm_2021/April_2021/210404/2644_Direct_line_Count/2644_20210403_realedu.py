

"""
BFS로 접근 / dfs도 되긴 함.
-> 인접 리스트 풀이 방식

"""
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())
lst = [[] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]
dist = [0] * (n + 1)

def bfs():
    Q = deque()
    Q.append(a)

    while Q:
        cur = Q.popleft()

        if cur == b:
            return dist[cur]

        for i in lst[cur]: # 부모의 자식들에 대해 체크
            if dist[i] == 0:
                Q.append(i)
                dist[i] = dist[cur] + 1

    return -1

for _ in range(m):
    x, y = map(int, input().split())
    # 트리 구조에서 양방향이 되게끔
    lst[x].append(y)
    lst[y].append(x)


print(bfs())
