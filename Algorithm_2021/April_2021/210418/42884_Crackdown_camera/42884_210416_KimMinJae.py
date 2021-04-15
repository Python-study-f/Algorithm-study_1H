from heapq import heappush, heappop
def solution(routes):
    q=[]
    for st, ed in routes:
        heappush(q,(ed,st))
    cam={}
    while q:
        e, s= heappop(q)
        flag=False
        for k in cam.keys():
            if s<=k:
                flag=True
                break
        if not flag:
            cam[e]=True
        
    return len(cam.keys())

print(solution(	[[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))