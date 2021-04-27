T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    time_lst = []
    for _ in range(N):
        time_lst.append(int(input()))
    #하한, 상한 초기화
    left, right = 1, max(time_lst)*M
    result = 0
    while left <= right:
        mid = (left + right)//2
        people = 0
        # 총 소요된 시간에서 각 심사위원이 맡은 사람의 수의 합이 M을 넘어야한다.
        # while문이 끝나고나면 조건을 충족하는 시간 중 가장 작은 값이 결과 값으로 저장된다.
        for t in time_lst:
            people += mid//t
            # M을 넘는다면 조건을 충족하는 시간으로 result에 저장하고 상한 값을 낮춘다.
            if people >= M:
                result = mid
                right = mid -1
                break
        # M을 넘지 못한다면 시간의 값이 커져야하므로 하한 값을 높인다.
        if people < M:
            left = mid + 1
    print('#{} {}'.format(tc, result))
