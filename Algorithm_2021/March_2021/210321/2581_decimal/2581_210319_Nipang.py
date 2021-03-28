# 백준 소수 문제

def solution():
    M = 1
    N = 15
    prime = []
    notPrime = []
    #Append every number between M and N
    for a in range(M,N+1):
        prime.append(a)
    for i in range(2,N):
        if i in prime:
            for b in range(2,N):
                notPrime.append(i*b)
                setNotPrime = set(notPrime)
                setPrime = set(prime)
                setPrime = setPrime - setNotPrime
    notprime = list(setNotPrime)
    prime = list(setPrime)
    sumPrime = sum(prime)
    # 소수가 없을 경우
    if not prime:
        sumPrime = -1
    # print prime
    #print(prime)
    # sum prime
    print(sumPrime)
    # smallest prime
    print(prime[0])

if __name__  == "__main__" :
    print(solution())