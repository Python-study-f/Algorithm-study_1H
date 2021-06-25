def solution(citations):
    citations.sort()
    length = len(citations)
    for idx, c in enumerate(citations):
        level = length - idx
        if c >= level:
            return level
    return 0
