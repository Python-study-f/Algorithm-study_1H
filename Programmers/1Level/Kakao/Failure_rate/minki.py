def solution(N, stages):
    answer = []
    stage_count = {i: 0 for i in range(1, N + 1)}
    stage_freq = []
    for stage in stages:
        if stage != N + 1: # stage 에서 완료된것은 빼기 위해서
            stage_count[stage] += 1
    users = len(stages)
    for key, value in stage_count.items():
        if users != 0: # 각 stage 마다 남아있는 user 수가 0이 아닐때
            stage_freq.append((key, value/users))
            users = users - value # 각 stage 를 지나면서 그 stage 에 있는 user 수를 빼준다
        else: # 단계에 남에 있는 user 수가 0 일때
            stage_freq.append((key, 0))
    stage_freq.sort(key = lambda user: (-user[1], user[0]))
    answer =[x[0] for x in stage_freq]
    return answer