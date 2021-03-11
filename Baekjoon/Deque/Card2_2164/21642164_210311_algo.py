from collections import deque

n=int(input())
temp=[i for i in range(1,n+1)]
q=deque(temp)
while len(q)>1:
    #print(q)
    q.popleft()
    q.append(q.popleft())
print(q.pop())
