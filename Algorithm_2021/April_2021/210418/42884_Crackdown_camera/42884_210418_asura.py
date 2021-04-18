'''
def solution(routes):
    routes.sort(key=lambda x:x[1])
    # [[-18, -13], [-14, -5], [-5, -3], [-20, 15]]
    ans = 0
    lim =  -30001

    for route in routes:
        if route[0] <= lim:
            continue
        ans += 1
        lim = route[1]

    return ans
'''
def solution(routes):
    ans = 0
    routes.sort(key=lambda x:x[1])
    lst_len = len(routes)
    check = [0] * lst_len

    for i in range(lst_len):
        if check[i] == 0:
            camera = routes[i][1]
            ans += 1

        for j in range(i+1,lst_len):
            if routes[j][0] <= camera <= routes[j][1] and check[j] == 0:
                check[j] = 1

    return ans
