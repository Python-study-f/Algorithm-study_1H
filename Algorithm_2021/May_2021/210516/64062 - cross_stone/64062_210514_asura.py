def solution(stones, k):
    # 풀이 : 이진탐색
    def check(mid,itv):
        cnt = 0

        for stone in stones:
            if stone < mid:
                cnt += 1
            else:
                cnt = 0

            if cnt ==  itv:
                return True
        return False

    answer = 0
    left, right = 1, max(stones) # 사람에 대한 이진탐색이므로 최소 0명 최대 돌 크기만큼

    while left <= right:
        middle = (left + right) // 2

        if not check(middle, k):
            left = middle + 1
        else:
            right = middle -1

    answer = left - 1

    return answer