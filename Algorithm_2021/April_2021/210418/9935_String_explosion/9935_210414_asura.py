# 1. Brute_Force 시간초과
'''
my_str = str(input())
find_str = str(input())
str_len = len(find_str)

while my_str:
    if find_str in my_str:
        if len(find_str) == len(my_str):
            my_str = "FRULA"
            break

        idx = my_str.index(find_str)

        my_str = my_str[:idx] + my_str[idx+str_len:len(my_str)]
    else:
        break

print(my_str)
'''

# 결국 인터넷 보고 풀음 ㅠㅠ,, 떠오르지 않음
# 링크 참조
# https://ksshlee.github.io/baekjoon/%EB%B0%B1%EC%A4%80-9935-%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%8F%AD%EB%B0%9C/
# 프로그래머스에서도 백준에서도 이런 문제를 많이 풀어본 거 같은데
# 이런 문제는 실력이 늘지 않는 거 같다.. 나중에 문제를 모아서 한번 풀어야겠다


my_str = str(input())
find_str = str(input())


st = []

for i in my_str:
    st.append(i)


    if len(st) >= len(find_str):
        flag = True

        for j in range(-1,(-len(find_str))-1,-1):
            if st[j] != find_str[j]:
                flag = False #하나라도 다를 경우
                break

        if flag:
            cur = 0
            while cur < len(find_str):
                st.pop()
                cur += 1

if len(st) == 0:
    print("FRULA")
else:
    print(''.join(st))
