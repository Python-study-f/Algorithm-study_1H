
"""
visit(nx, ny) + visit(x, y)가 아닌 
visit(x, y, nx, ny) + visit(nx, ny, x, y)여야하는 이유
-> 캐릭터가 처음 걸어본 길의 길이를 구하는 것.
"""
def solution(dirs):
    dir = {"L":(-1, 0), "U":(0, 1), "R":(1, 0), "D":(0, -1)}
    visit = set() 
    distance = 0
    x, y = 0, 0
    
    for d in dirs:
        nx = x + dir[d][0]
        ny = y + dir[d][1]
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            """
            if (nx, ny) not in visit:
                visit.add((x, y))
                visit.add((nx, ny))
            """
            if (x, y, nx, ny) not in visit:
                visit.add((x, y, nx, ny))
                visit.add((nx, ny, x, y))
                distance += 1
            x, y = nx, ny
        
    return distance
