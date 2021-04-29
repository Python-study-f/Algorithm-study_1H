# 다리를 지나는 트럭 42583 프로그래머스
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    passed_truck = []
    passing_truck = []
    n = len(truck_weights)
    truck_weights = deque(truck_weights)
    sum_w = 0
    while True:
        answer += 1
        if truck_weights and (sum_w + truck_weights[0]) <= weight:
            tmp = truck_weights.popleft()
            sum_w += tmp
            passing_truck.append([tmp, 0])

        for t in passing_truck:
            t[1] += 1
        if passing_truck and passing_truck[0][1] >= bridge_length:
            tmp = passing_truck.pop(0)
            passed_truck.append(tmp)
            sum_w -= tmp[0]
        if len(passed_truck) == n:
            break

    return answer


b = 100
w = 100
t = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

print(solution(b, w, t))
