from collections import deque
def solution(begin, target, words):
    n = len(begin)
    answer = 0
    vis = {}
    q = deque([begin])
    rs = 0
    while q:
        rs += 1
        for _ in range(len(q)):
            cur = q.popleft()
            for word in words:
                if not vis.get(word):
                    cnt = 0
                    for i in range(n):
                        if cur[i] != word[i]:
                            cnt += 1
                    if cnt == 1:
                        if word == target:
                            return rs
                        else:
                            vis[word] = 1
                            q.append(word)
    return answer