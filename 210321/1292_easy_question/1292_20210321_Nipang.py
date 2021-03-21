def solution(A,B):
    numbers = []
    for i in range(B):
        nums = [i] * i
        for a in nums:
            numbers.append(a)
    del numbers[:A-1]
    del numbers[B:]
    #print(numbers)
    print(sum(numbers))
