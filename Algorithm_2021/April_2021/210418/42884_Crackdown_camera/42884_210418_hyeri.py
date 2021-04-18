def solution(routes):
    routes.sort(key=lambda x:x[1])
    prev = -30000
    ans = 0
    for car in routes:
        if prev < car[0]:
            prev = car[1]
            ans +=1
    return ans
