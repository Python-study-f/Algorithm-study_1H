import heapq
#이중 우선 순위 큐


#이중 우선순위 연산자 작동
def operator(l, a, b):
    # 연산자 확인
    # I일 경우 숫자 삽입
    if a =='I':
        heapq.heappush(l, int(b))
    # D일 경우 숫자 제거
    elif a == 'D':
        if b =='1':
            max=heapq.nlargest(1, l)[0]
            l.pop(max)
        else:
            heapq.heappop(l)
    #최대, 최솟값 출력
    lmin = heapq.nsmallest(1, l)[0]
    lmax = heapq.nlargest(1, l)[0]
    return h, lmin, lmax


if __name__ == '__main__':
    h= []
    hmin = 0
    hmax = 0
    parameters = []
    x,y = parameters.split()
    h, hmin, hmax = operator(h, x, y)
    #리스트 길이가 0일경우 empty 출력
    if len(h) == 0:
        print("EMPTY")
    else:
        print(hmax, hmin)