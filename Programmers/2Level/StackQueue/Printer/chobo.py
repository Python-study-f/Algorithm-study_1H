def solution(priorities, location):
    answer = 0
    wait_queue = [(idx, value) for idx, value in enumerate(priorities)]
    
    while True:
        # 맨 앞의 대기목록에 있는 종이를 빼낸다.
        paper = wait_queue.pop(0)
        # 우선순위가 작은 경우
        if any(paper[1] < temp[1] for temp in wait_queue):
            wait_queue.append(paper)
        
        # 우선순위가 제일 높은 경우
        else:
            answer += 1             # 몇 번째로 출력되는지 확인해줌
            if paper[0] == location:
                return answer
    
priorities = [1, 1, 9, 1, 1, 1]
location = 5

print(solution(priorities, location))