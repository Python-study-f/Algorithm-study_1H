# w : 가로, h : 세로
def solution(w, h):
    total_paper = w * h
    temp_paper = w + h
    answer = 0

    if w > h:
        pass
    else:
        w, h = h, w
    
    # w가 최대공약수로 변환되어 나옴
    # 유클리드 호제법
    while h > 0:
        w, h = h, w % h
    
    answer = total_paper - temp_paper + w

    return answer


print(solution(8, 12))
