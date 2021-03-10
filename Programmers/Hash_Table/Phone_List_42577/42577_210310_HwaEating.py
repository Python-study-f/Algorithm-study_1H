def solution(pb):
    pb.sort(key=lambda x:len(x))
    ht = {}
    prev = len(pb[0])
    for p in pb:
        for i in range(prev+1):
            if ht.get(p[:i]):
                return False
        prev = len(p)
        ht[p] = 1
    return True