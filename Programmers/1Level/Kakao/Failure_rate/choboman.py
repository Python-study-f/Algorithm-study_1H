# 실패율 = 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수

# 1. for i in range(1, N + 1) 반복
# 2. 1이 몇개인지, 2가 몇개인지, ..
# 3. i의 갯수 -> 해당 스테이지 실패한 사람의 수
# 4. failure = [] , append((실패 수, 도달 플레이어 수))


def solution(N, stages):
    stage_cnt = len(stages)

    answer = []                                                     # 이중 for문을 만들 것임 [[스테이지, 실패율], [], [], .. ]


    for i in range(1, N + 1):                                       # N회 반복
        fail_cnt = stages.count(i)
        if fail_cnt == 0:                                           # 스테이지에 도달한 유저가 없을 경우, 해당 스테이지 실패한 사람은 0명
            answer.append([i, 0])                                   # 실패한 사람 수
        else:
            fail_cnt = stages.count(i)                              # stages 배열에서 i란 숫자를 가지고 있는 사람의 수 -> 실패한 사람 수
            answer.append([i, fail_cnt / stage_cnt])
            stage_cnt -= fail_cnt

    answer.sort(key=lambda x: x[1], reverse=True)                   # 각 인덱스에 있는 배열에서 실패율 key값으로 잡고 내림차순 했음

    answer = [i[0] for i in answer]                                 # [스테이지, 실패율] 에서 실패율 기준으로 sort 되었으니 스테이지들을 추출하여 리스트로 생성
    
    return answer