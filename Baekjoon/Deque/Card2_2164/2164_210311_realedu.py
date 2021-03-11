"""
1. 제일 위 카드는 버린다.
2. 제일 위 카드를 제일 아래 카드 밑으로 옮긴다.
	
1, 2를 반복하여 마지막에 남는 카드는?

==> collections의 deque 활용
	- d 변수 deque() 선언
	- N 길이 만큼 d에 append
	- deque.popleft(), deque.append() 하고자 했으나 
	append()의 경우 popleft()를 한번 더 해야하고, 그렇게 되면 예외적인 경우들로 인해 해결이 힘들어짐.
그래서 rotate(-1)을 이용하여 왼쪽으로 회전하는 것을 이용.
"""

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
