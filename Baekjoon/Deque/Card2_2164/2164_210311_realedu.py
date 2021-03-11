from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
d = deque()

for i in range(1, N + 1):
    d.append(i)
# print(*d) # 1 2 3 4 5

if len(d) == 1:
    print(*d)
else: # 길이가 2이상인 경우
    while True:
        if len(d) == 1:
            print(*d)
            break
        else:
            d.popleft()
        d.rotate(-1) # left rotation
