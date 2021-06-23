def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i: 
            return len(citations) - i
    return 0

# 정렬을 하면 i 번째는 i보다 작은 논문이 i-1개 있다는 뜻
