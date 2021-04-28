from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    bridge_weight = sum(bridge) # 
    truck_weights = deque(truck_weights)
    
    while bridge:
        bridge_weight -= bridge[0]
        bridge.popleft()
        answer += 1
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                bridge_weight += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
                
    """ 시간초과 (sum(bridge_length))
    while bridge_length:
        bridge_length.popleft()
        answer += 1
        if truck_weights:
            if sum(bridge_length) + truck_weights[0] <= weight:
                bridge_length.append(truck_weights.popleft())
            else:
                bridge_length.append(0)
    """
    return answer
