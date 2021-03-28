# Run time error
# https://www.acmicpc.net/problem/2581
import pdb

import math

def is_prime(N):
    if N%2 == 0 and N != 2:
        return False
    elif N <=1:
        return False
    else:
        for i in range(3,math.floor(math.sqrt(N)) + 1,2):
            if N%i ==0:
                return False
    return True

def solution(n1, n2):
    tot = 0

    if n1 == n2:
        if is_prime(n1):
            print(n1)
            print(n1)
            return
        else:
            print(-1)
            return

    elif n1 % 2 == 1:
        if n1 == 1:
            tot = 2
            minimum = 2
        for i in range(n1, n2 + 1, 2):
            if is_prime(i):
                if tot == 0:
                    minimum = i
                tot += i
    else:
        if n1 == 2:
            tot = 2
            minimum=2

        for i in range(n1+1, n2 + 1, 2):
            if is_prime(i):
                if tot == 0:
                    minimum = i
                tot += i

    if tot == 0:
        print(-1)
        return
    else:
        print(tot)
        print(minimum)
        return

n = int(input())
m = int(input())
solution(n, m)
