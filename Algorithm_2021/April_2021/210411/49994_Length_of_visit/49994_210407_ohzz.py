# 방문 길이 49994


def solution(dirs):
    answer = []
    dic = {"U": [0, 1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}

    x, y = 0, 0
    for i in dirs:
        nx, ny = dic[i][0] + x, dic[i][1] + y
        if abs(nx) > 5 or abs(ny) > 5:
            continue
        if [[nx, ny], [x, y]] not in answer:
            if [[x, y], [nx, ny]] not in answer:
                answer.append([[nx, ny], [x, y]])
                answer.append([[x, y], [nx, ny]])
        x = nx
        y = ny
    return len(answer) // 2
