from collections import deque

def bfs(x):
    dq = deque([x])

    while dq:
        cur = dq.popleft()

        for j in range(1,n+1):
            if data[cur][j] == 1 and  root[j] == 0:
                root[j] = root[cur] + 1
                dq.append(j)

n = int(input())
start, des = map(int, input().split())
m = int(input())

data = [[0] * (n+1) for _ in range(n+1)] # m+1은 첫번째 리스트 비우고 나머지 리스트로 구현하기 위해서 비움
root = [0] * (n+1)

for i in range(m):
    a, b = map(int,input().split())
    data[a][b] = data[b][a] = 1

bfs(start)
ans = root[des]
if ans == 0:
    print("-1")
else:
    print(ans)
