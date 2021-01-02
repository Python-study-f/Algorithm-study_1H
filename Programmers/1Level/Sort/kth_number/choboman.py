def solution(array, commands):
    answer = []
    for i in commands:                      # [2, 5, 3] -> [4, 4, 1] -> [1, 7, 3]
        temp_arr = []
        for j in range(i[0] - 1, i[1]):     # temp_arr 만들기
            temp_arr.append(array[j])       # temp_arr 채우기
        temp_arr.sort()
        answer.append(temp_arr[i[2] - 1])
        temp_arr.clear()
    return answer
