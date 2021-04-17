from collections import deque
def solution(begin, target, words):
    answer = 0
    dq = deque()
    dq.append(begin)
    
    # bfs 탐색
    while len(dq) > 0:
        for qs in range(len(dq)):
            st = dq.popleft()
            if st == target:
                return answer
            for w in words:
                n = 0
                for i in range(len(st)):
                    if st[i] != w[i]:
                        n += 1
                    if n > 1:
                        break
                if n == 1:
                    dq.append(w)
            if len(dq) == 0 or answer > len(words):
                return 0
        answer += 1
    return answer
