"""
문자열 위치 조작 -> 한계가 있음.
-> 리스트로 변환
"""

# 1 ~ 9번 테스트 케이스까지는 잘 나오나 10번이 안나옴.. -> runtime error
# 따로 visit 처리를 해주지 않아서 그런가? 
"""
def dfs(d, cnt):
    global result

    if cnt == Count:
        result = max(int("".join(number)), result)
        return
    for i in range(0, l):
        for j in range(i + 1 , l):
            if number[i] <= number[j]:
                number[i], number[j] = number[j], number[i]
                dfs(i, cnt + 1)
                number[i], number[j] = number[j], number[i]

for t in range(T):
    # number, Count = map(int, input().split())
    number, Count = input().split()
    number = list(number)
    number_slice = number[:]
    Count = int(Count)
    l = len(number_slice)
    visit = []

    result = 0
    dfs(0, 0)

    print("#{} {}".format(t+1, result))
"""


def dfs(cnt):
    global result, number

    if cnt == Count:
        result = max(result, int(''.join(number)))
        return

    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            number[i], number[j] = number[j], number[i]

            temp_key = (''.join(number), cnt)

            if temp_key not in visit:
                visit.add(temp_key)
                dfs(cnt + 1)
            number[i], number[j] = number[j], number[i]

T = int(input())

for t in range(1, T + 1):
    # number, Count = map(int, input().split())
    number, Count = input().split()
    number = list(number)
    Count = int(Count)
    visit = set()
    result = 0

    dfs(0)
    print("#{} {}".format(t, result))
