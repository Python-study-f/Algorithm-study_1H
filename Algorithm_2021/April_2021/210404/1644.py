from math import sqrt
era = [1]*(4000001)
era[0] = 0
era[1] = 0

primes = []

for i in range(2,4000000):
    if era[i]:
        primes.append(i)
        time = 2
        while i*time <= 4000000:
            era[i*time] = 0
            time += 1

tar = int(input())
n = len(primes)
sufsum = [0]*(n+1)
for i in range(1,n):
    sufsum[i] = sufsum[i-1] + primes[i-1]

ans = 0
l = 0
for r in range(1,n+1):


    if sufsum[r] - sufsum[l] == tar:
        ans += 1
    
    while sufsum[r] - sufsum[l] > tar:
        l += 1
        if sufsum[r] - sufsum[l] == tar:
            ans += 1
            break

print(ans)