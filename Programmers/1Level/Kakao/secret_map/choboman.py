

def getEjin(n):
    ans = ''
    while True:
        div = (n % 2)
        n = (n // 2)
        if n > 1:
            ans = str(div) + ans
        else:
            ans = int(str(n) + str(div) + ans)
            break
    return ans


def solution(n, arr1, arr2):
    # map1 = [ [0] * n for _ in range(n)]         # map 1 생성 (n x n)
    # map2 = [ [0] * n for _ in range(n)]         # map 1 생성 (n x n)
    for i in range(len(arr1)):                              # 9. 20, 28, 18, 11
        arr1.insert(i, str(getEjin(arr1[i])).zfill(5))
        arr1.pop(i + 1)
    for i in range(len(arr2)):
        arr2.insert(i, str(getEjin(arr2[i])).zfill(5))
        arr2.pop(i + 1)
    


    
    return arr1, arr2

'''
def solution(n, arr1, arr2):
    answer = []
    for decimal1, decimal2 in zip(arr1, arr2):
        binary12 = str(bin(decimal1 | decimal2))[2:]
        binary12 = '0' * (n - len(binary12)) + binary12
        binary12 = binary12.replace('1', '#')
        binary12 = binary12.replace('0', ' ')
        answer.append(binary12)
    return answer
'''
