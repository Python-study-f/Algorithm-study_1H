def solution(n):
    answer = ''
    dict1 = {1: '1', 2: '2', 0: '4'}
    while n > 0:
        rest = n % 3
        n = int(n / 3)
        if rest == 0:
            n = n - 1
        answer = str(dict1[rest]) + answer
    
    return answer

print(solution(9))

# dict1 = {1: '1', 2: '2'}

# print(dict1[2])
