def solution(s):
    temp_list = []
    new_s = s.split(' ')
    for word in new_s:
        size = len(word)
        for i in range(size):
            if i % 2 == 0:
                temp_list.append(word[i].upper())
            else:
                temp_list.append(word[i].lower())

        temp_list.append(' ')
    answer = ''.join(temp_list)
    return answer[:-1]
