N = int(input())
count = 0

while True:
    if N%5 == 0:
        count = count + N//5
        print(count)
        break
    N = N - 3
    count += 1
    if N < 0:
        print(-1)
        break
