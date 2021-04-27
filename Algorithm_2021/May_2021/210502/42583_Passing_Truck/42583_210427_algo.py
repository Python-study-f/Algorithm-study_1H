def solution(bridge_length, weight, truck_weights):
    answer = 0 #시간
    t_list = [] # 트럭저장하는 큐 (리스트로 만듬) - 다리상황과 동일하다고 생각하면 됨
    # 트럭뽑는 함수
    for i in truck_weights:       # [7,4,5,6]
        q_truck =i                       
        while q_truck !=0:
            if len(t_list) == bridge_length:          # 길이가 같으면 pop
                t_list.pop()                              
            if (sum(t_list)+q_truck)<=weight:             # 크기가 weight보다 작으면 돌린다.
                t_list.insert(0,q_truck)                  # 첫번째 인덱스에 q_truck을 삽입
                q_truck=0                                 # 다음으로 넘어감 
                answer+=1                                 
            else:                                         #크기가 더작으니 삽입
                t_list.insert(0,0)
                answer+=1
                
    answer = answer+bridge_length               
                
    return answer
