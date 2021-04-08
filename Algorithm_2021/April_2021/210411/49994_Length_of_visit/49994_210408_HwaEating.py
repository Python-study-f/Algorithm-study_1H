def makeXY(x,y,ht):
    if not ht.get(x):
        ht[x] = {}
    if not ht[x].get(y):
        ht[x][y] = {}

def solution(dirs):
    answer = 0
    history = {}
    x,y = 0,0
    makeXY(x,y,history)
    for d in dirs:
        if d == 'U':
            if x+1 <= 5:
                if not history[x][y].get(d):
                    answer += 1
                    history[x][y][d] = 1
                    x += 1
                    makeXY(x,y,history)
                    history[x][y]['D'] = 1
                else:
                    x += 1
                
        elif d == 'D':
            if x-1 >= -5:
                if not history[x][y].get(d):
                    answer += 1
                    history[x][y][d] = 1
                    x -= 1
                    makeXY(x,y,history)
                    history[x][y]['U'] = 1
                else:
                    x -= 1
                
        elif d == 'R':
            if y+1 <= 5:
                if not history[x][y].get(d):
                    answer += 1
                    history[x][y][d] = 1
                    y += 1
                    makeXY(x,y,history)
                    history[x][y]['L'] = 1
                else:
                    y += 1
                
        else:
            if y-1 >= -5:
                if not history[x][y].get(d):
                    answer += 1
                    history[x][y][d] = 1
                    y -= 1
                    makeXY(x,y,history)
                    history[x][y]['R'] = 1
                else:
                    y -= 1
            
    return answer