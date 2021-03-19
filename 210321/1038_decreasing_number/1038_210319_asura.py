# N = int(input())
# cnt = 0
# i = 0
# while 1:
#     i += 1
#
#     if N > 22:
#         print(-1)
#         break
#
#     my_str = list(str(i))
#
#     if my_str != sorted(my_str, reverse=True): #전반적인 감소하는 수인지 아닌지
#         continue
#
#     if len(my_str) != len(set(my_str)): # 110 222 등 감소하지 않는 숫자.
#         continue
#
#     cnt +=1
#     if cnt == N:
#         print(i, end= '')
#         break
# if N == 0:
#     print(0)
'''
1. 문제를 잘못 이해해서 뻉뺑 돌았음. N의 감소하는 숫자의 번호가 아닌 루프를 도는 범위라고 생각함
2. ...빡치넹?
'''



def solve(n):
    cnt = 0
    num = 1

    while True:
        my_num = str(num)
        flag = True

        if len(my_num) == 1: # 0~9까지 숫자
            pass
        else:
            for i in range(1, len(my_num)):
                if int(my_num[i-1]) > int(my_num[i]): # 감소하는 수
                    continue
                else:
                    first = my_num[:i-1]
                    second = str(int(my_num[i-1]) + 1)
                    last = "0" + my_num[i+1:]
                    num = int(first + second + last)
                    print(my_num, first, second, last, num) # 두자리 수는  first가 없다.
                    flag = False
                    break
        if flag:
            cnt += 1
            if cnt == n:
                return num
            num += 1

N = int(input())

if N >= 1023: # 1022 : 987654321 // 10c1 + 10c2 + 10c3 ... + 10c1 = 2^10 -1
    print(-1)
elif N == 0:
    print(0)
else:
    print(solve(N))


'''
print(my_num, first, second, last, num) 에 대한 Log
11  2 0 20
22  3 0 30
33  4 0 40
44  5 0 50
55  6 0 60
66  7 0 70
77  8 0 80
88  9 0 90
99  10 0 100
100 1 1 0 110
110  2 00 200
200 2 1 0 210
211 2 2 0 220

질문 Q: 백트래킹는 언제 쓰는 것인가? 문제를 풀어봐야 나오는 것인가?
'''