def solution(n, lost, reserve):
    answer = 0
    a = {}  # 딕셔너리 생성
    for i in range(1, n + 1):
        a[i] = 1  # {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    for i in lost:  # i = 2, 4
        a[i] -= 1  # {1: 1, 2: 0, 3: 1, 4: 0, 5: 1}
    for i in reserve:  # i = 1, 3, 5
        a[i] += 1  # {1: 2, 2: 0, 3: 2, 4: 0, 5: 2}
    for i in range(1, n + 1):
        if a[i] > 1:
            if i > 1 and a[i - 1] == 0:  # i가 1일때는값이 없으니 1 > 1
                a[i - 1] += 1
                a[i] -= 1
            elif i < n and a[i + 1] == 0:  # i가 마지막일떄는 값이 없으니 i < n
                a[i + 1] += 1
                a[i] -= 1
    # print(a) {1: 1, 2: 1, 3: 1, 4: 1, 5: 2}
    for i in range(1, n + 1):
        if a[i] > 0:
            answer += 1
    # answer = 5
    return answer
