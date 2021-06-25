# h-index 42747 프로그래머스


def solution(citations):
    h = len(citations)
    citations.sort(reverse=True)
    while h:
        cnt = 0
        for c in citations:
            if c >= h:
                cnt += 1
            if cnt >= h:
                return h
        h -= 1
    return h


print(solution([25, 8, 5, 3, 3]))
