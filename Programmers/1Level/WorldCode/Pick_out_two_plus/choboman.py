def solution(numbers):
    answer = []
    temp_num = 0
    for i in range(len(numbers)):                       # numbers 길이만큼 반복
        for j in range((i+1), len(numbers)):            # i+1부터  numbers 길이까지 반복
            temp_num = numbers[i] + numbers[j]
            if temp_num in answer:
                continue
            else:
                answer.append(temp_num)
        
        answer.sort()
    return answer
