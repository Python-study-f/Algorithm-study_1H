from collections import deque
# 낮은 숫자에서 높은 숫자로 올라가는게 아닌 반대로 높은 숫자에서 낮은 숫자로 내려오는 방식을 택했습니다


# 시간 추가 없이 순간이동으로 이동할 수 있는 모든 포인트를 연산합니다
def teleporting(a,b):
    count = 0
    while True:
        if count < len(a):
            if a[count]%2 == 0 and b.count(int(a[count]/2)) == 0:
                a.append(int(a[count]/2))
                b.append(int(a[count]/2))
        elif count == len(a):
            break
        count += 1
    return a, b


# 수빈이가 동생을 만났는지 확인합니다
def reached(a, b):
    tmp = 0
    if b.count(a) == 1:
        tmp = 1
    return tmp


# 1초 후 x+1, x-1 위치로 이동할 수 있는 포인트 들을 연산합니다.
def updatep(a, b):
    c = deque()
    for i in a:
        if b.count(i+1) == 0:
            c.append(i+1)
            b.append(i+1)
        if b.count(i-1) == 0 and (i-1) > 0:
            c.append(i-1)
            b.append(i-1)
    return c, b


# 최단시간 검색
def findt(a, b):
    t = 0
    yay = a
    tmp = 0
    p = deque([b])
    pvisited = deque([b])
    while tmp == 0:
        p, pvisited = teleporting(p, pvisited)
        tmp = reached(yay,pvisited)
        print(pvisited)
        t+=1
        p, pvisited =updatep(p,pvisited)
    return t-1


if __name__ == '__main__':
    n=13
    k=60
    t=findt(n, k)
    print(t)
