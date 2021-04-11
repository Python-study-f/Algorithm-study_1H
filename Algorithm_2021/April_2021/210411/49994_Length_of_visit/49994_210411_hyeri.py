
def solution(dirs):
    dic = {"U": [-1, 0], "D": [1, 0], "R": [0, 1], "L": [0, -1]}
    x = 0
    y = 0
    answer = 0
    visit = set()
    
    for d in dirs:
        tx = x + dic[d][0]
        ty = y + dic[d][1]
        
        if tx < -5 or ty < -5 or tx > 5 or ty > 5:
            continue
        if (x, y, tx, ty) not in visit:
            visit.add((x, y, tx, ty))
            visit.add((tx, ty, x, y)) 
            answer += 1
        x = tx
        y = ty
            
    return answer
