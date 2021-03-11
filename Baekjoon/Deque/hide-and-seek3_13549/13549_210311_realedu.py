"""
=> (x-1, x+1, 2*x)는 이 3개 그대로.

=> 0초 후에 2*X의 위치로 이동하는 것을 어떻게 구현할 것인가?
: appendleft()를 통해 2*X의 위치를 우선적으로 처리한다.
"""

from collections import deque
import sys

def BFS(arr, N, K):
    Q = deque()
    Q.append(N) # 현재 수빈이의 위치 N 정보 넣음

    while Q:
        x = Q.popleft()
        if x == K: # 동생의 위치에 도달했다면
            return arr[x]
        for nx in (x-1, x+1, 2*x): # 
            # not arr[nx]가 없으면 -> arr의 배열 범위를 넘어섬.
            if 0 <= nx < 100001 and not arr[nx]: 
                if nx == 2 * x and x != 0: # 2*x의 경우 -> 0초
                    arr[nx] = arr[x]
                    Q.appendleft(nx)
                else:                      # x-1 또는 x+1인 경우 -> +1초
                    arr[nx] = arr[x] + 1
                    Q.append(nx)

N, K = map(int, sys.stdin.readline().split())
visit = [0] * 100001
print(BFS(visit, N, K))
