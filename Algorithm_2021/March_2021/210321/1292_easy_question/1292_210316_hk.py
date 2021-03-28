#list를 쓰는 방식, 안쓰는 방식 두가지로 문제 풀었습니다.
def addarray(a,b):
    if a == b:
        count=1
        tcount=1
        while a > tcount:
            count += 1
            tcount = int((count + 1) * count / 2)
        result = count
    elif a > b:
        result = 0
    else:
        count1=1
        lowercount=1
        while a > lowercount:
            count1 += 1
            lowercount = int((count1+1)*count1/2)
        res1 = lowercount - a
        count2=1
        uppercount=1
        while b > uppercount:
            count2 += 1
            uppercount = int((count2 + 1) * count2 / 2)
        res2=uppercount-b
        result=count1*(res1+1)+count2*(count2-res2)
        if count1 == count2:
            result = count1*(res1 - res2+1)
        elif count2-count1 > 1:
            for i in range(count1+1,count2):
                result += i*i
    return result

A, B = map(int, input().split())
a =addarray(A,B)
print((a))

#list 쓰는 풀이법
numlist = []
for i in range(1, 50):
    numlist += [i] * i
a=sum(numlist[A - 1:B])
print((a))