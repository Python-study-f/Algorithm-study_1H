def solution(N, stages):
    key_list = []
    fail = {}
    length = len(stages)
    for i in range(1, N + 1):
        stage_count = stages.count(i)
        if length == 0:
            fail[i] = 0
        else:
            fail[i] = stage_count / length
            length -= stage_count
    # 정렬 기준이 item[1] = value 니까 value 로 정렬하겠다  ,, ?
    fail2 = sorted(fail.items(), reverse=True, key=lambda item: item[1])  # 내림차순
    # print(fail2) [(3, 0.5), (4, 0.5), (2, 0.42857142857142855), (1, 0.125), (5, 0.0)]
    for i in range(N):
        key_list.append(fail2[i][0])
    return key_list


n = 4
stage = [4, 4, 4, 4, 4]
print(solution(n, stage))