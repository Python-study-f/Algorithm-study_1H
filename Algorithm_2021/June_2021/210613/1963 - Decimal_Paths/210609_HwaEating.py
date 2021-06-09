from collections import deque

era = [1 for _ in range(10000)]
era[0] = 0
era[1] = 0
for i in range(2,101):
    if era[i]:
        times = 2
        while i*times < 10000:
            era[i*times] = 0
            times += 1

primes = []
for i in range(1000,10000):
    if era[i]:
        primes.append(i)

def bfs(s,e):
    ans = 0
    queue = deque()
    queue.append(s)
    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            if cur == e:
                return ans
            for prime in primes:
                if vis[prime] == 0:
                    strP = str(prime)
                    cnt = 0
                    for i in range(4):
                        if strP[i] == cur[i]:
                            cnt += 1
                    if cnt == 3:
                        vis[prime] = 1
                        queue.append(strP)
        ans += 1

n = int(input())
for _ in range(n):
    s,e = input().split()
    vis = [0]*10000
    vis[int(s)] = 1
    print(bfs(s,e))