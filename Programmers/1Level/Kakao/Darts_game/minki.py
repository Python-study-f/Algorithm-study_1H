import re

def solution(dartResult):
    answer = 0
    answerArr = []
    regex = re.compile('\d+|[A-Z]|[\*#]?')
    found = regex.findall(dartResult)
    for item in found: 
        if item.isdigit():
            answerArr.append(int(item));
        else:
            if item == 'S': 
                answerArr[-1] = answerArr[-1] ** 1
            elif item == 'D':
                answerArr[-1] = answerArr[-1] ** 2
            elif item == 'T':
                answerArr[-1] = answerArr[-1] ** 3
            elif item == '*':
                answerArr[-1] *= 2;
                if len(answerArr) > 1:
                    answerArr[-2] *= 2
            elif item == '#':
                answerArr[-1] *= -1;
    answer = sum(answerArr)
    return answer