# 1 >> 1, 2, 3, 4, 5,                   1, 2, 3, 4, 5
# 2 >> 2, 1, 2, 3, 2, 4, 5,             2, 1, 2, 3, 2, 4, 2, 5
# 3 >> 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,    3, 3, 1, 1, 2, 2, 4, 4, 5, 5
# answer = [1, 3, 2, 4, 2]


def solution(answers):
    answer = []
    temp_answer = []
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    cnt1, cnt2, cnt3 = 0, 0, 0
    
    for i in range(len(answers)):                                                # answer 길이
        if answers[i] == first[i % len(first)]:
            cnt1 += 1
        if answers[i] == second[i % len(second)]:
            cnt2 += 1
        if answers[i] == third[i % len(third)]:
            cnt3 += 1
    
    temp_answer = [cnt1, cnt2, cnt3]
    
    for idx, score in enumerate(temp_answer):
        if score == max(temp_answer):
            answer.append(idx + 1)
            
    return answer


