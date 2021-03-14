from collections import deque

def solution(N):
    # left = top
    # right = bottom
    queue = deque(range(1, N+1))

    while len(queue) > 1:
        card2throw = queue.popleft()
        card2move = queue.popleft()
        queue.append(card2move)

    return queue.pop()
