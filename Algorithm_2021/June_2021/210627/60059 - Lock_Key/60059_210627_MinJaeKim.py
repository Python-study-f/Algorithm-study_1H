en = enumerate
def check(mp, y, x, r):
    for i in range(y, y + r):
        for j in range(x, x + r):
            #print(r)
            #print(mp[i][j], end = '')
            if not mp[i][j] or (mp[i][j] == 2):
                return False
        #print()
    #print()
    return True


def rot(key):
    return [el[:] for el in zip(*key[::-1])] 

def bound(y, x, r):
    if 0 <= y < 70 and 0 <= x < 70:
        return True
    return False
    
def solution(key, lock):

    k = len(key)
    l = len(lock)

    defaul = [ [0] * 70 for _ in range(70)]
    for idx, h in en(range(25, 25 + l)):
        for bdx, w in en(range(25, 25 + l)):
            defaul[h][w] = lock[idx][bdx]
    
        
    for i in range(70):
        for j in range(70):
            # i, j 가 시작 좌표
            for _ in range(4):
                key = rot(key)
                #print(*key, sep = '\n')
                #print()
                mp = [el[:] for el in defaul]
                #print(*mp, sep = '\n')
                out = False
                for idx, a in en(range(i, i + k)):
                    for bdx, b in en(range(j, j + k)):
                        if not bound(a, b, l):
                            out = True
                            break
                        mp[a][b]+= key[idx][bdx]
                    if out:
                        break
                #print(*mp, sep = '\n')
                if check(mp, 25, 25, l):
                    return True

    return False


#print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))