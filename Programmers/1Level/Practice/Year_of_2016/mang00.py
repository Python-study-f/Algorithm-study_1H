def solution(a, b):
    answer = ''
    ml = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    ms = 0
    for i in range(a - 1):
        ms += ml[i]
    ms = ms + b + 4
    a = ms % 7
    answer = day[a]
    return answer
