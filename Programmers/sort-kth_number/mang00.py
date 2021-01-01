def solution(array, commands):
    answer = []
    for command in commands:  # command = [2,5,3]
        array3 = array[command[0] - 1:command[1]]  # array3 = [5,2,6,3]
        array3.sort()  # array3 = [2,3,5,6]
        answer.append(array3[command[2] - 1])
    return answer
