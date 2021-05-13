# 징검다리 건너기 64062 프로그래머스

def isValidJump(stones, k, mid):
    cnt = 0
    for s in stones:
        if s - mid <= 0:
            cnt += 1
        else:
            cnt = 0
        if cnt >= k:
            return False
    return True

def solution(stones, k):
    answer = 0
    lt = 0
    rt = max(stones) + 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if isValidJump(stones, k, mid):
            lt = mid + 1
        else:
            rt = mid - 1
    answer = lt
    return answer


arr = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
t = 3

print(solution(arr, t))