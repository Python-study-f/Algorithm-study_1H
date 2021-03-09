from collections import deque

dq = deque([i+1 for i in range(int(input()))])

cnt = 1

while len(dq) != 1:
    if cnt & 1 :
        dq.popleft()
    else:
        dq.append(dq.popleft())
    cnt+=1

print(dq[0])

