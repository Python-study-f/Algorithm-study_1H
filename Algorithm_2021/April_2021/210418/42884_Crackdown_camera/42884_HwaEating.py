def solution(routes):
    answer = 0
    routes.sort()
    routes.sort(key=lambda x:x[1])
    idx = 0
    n = len(routes)
    while idx < n:
        answer += 1
        endpoint = routes[idx][1]
        while idx < n and endpoint >= routes[idx][0]:
            idx += 1
    
    return answer