def solution(citations):
    citations.sort()
    n = len(citations)
    h = 0

    for idx,cit in enumerate(citations):
        if cit >= n-idx:
            h = n-idx
            break
    return h