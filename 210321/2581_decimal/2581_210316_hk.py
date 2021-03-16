import math


def isitprime(N):
    if N%2 == 0 and N != 2:
        return False
    elif N <=1:
        return False
    else:
        for i in range(3,math.floor(math.sqrt(N)) + 1,2):
            if N%i ==0:
                return False
    return True


def mainfunc(A,B):
    count = 0
    total = 0
    minprime = 0
    if A == B:
        if isitprime(A):
            total = A
            minprime = A
            print(total)
            print(minprime)
        else:
            print(-1)
        return
    elif A % 2 == 1:
        a = range(A, B + 1, 2)
        if A == 1:
            total = 2
            minprime = 2
            count = 1
    else:
        a = range(A + 1, B + 1, 2)
        if A == 2:
            total = 2
            minprime = 2
            count = 1
    for i in a:
        if isitprime(i):
            total += i
            if count == 0:
                minprime = i
                count = 1
    if count == 0:
        print(-1)
    else:
        print(total)
        print(minprime)

a = int(input())
b = int(input())
mainfunc(a,b)
