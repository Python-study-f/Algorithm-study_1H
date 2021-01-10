def solution(s):
    answer = ''
    lst_s = list(map(str, s.split(' ')))            # 공백 기준으로 나눔
    for lst in lst_s:                               # try, hello, world
        for idx, i in enumerate(lst):
            if idx % 2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
        answer += ' '
                
    return answer[:-1]
