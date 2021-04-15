# 단속 카메라 42884


def solution(routes):
    answer = 0
    routes.sort()

    camera = routes[0][1]
    answer = 1

    for i in range(1, len(routes)):
        if camera >= routes[i][0]:
            camera = min(routes[i][1], camera)
        else:
            camera = routes[i][1]
            answer += 1

    return answer


# 오름차순 정리하고 camera가 앞 진입보다 크면 판단
#  -20                              15
#     -18     -13
#           -14     -5
# 카메라       -13 에 하나

#                   -5  -3
# 카메라                 -3에 하나
# 총 두개
