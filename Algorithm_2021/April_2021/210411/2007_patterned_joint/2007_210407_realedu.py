
"""
str[0:i]와 str[i:i*2] 비교 방법
-> aabcaabcaabcaabcaabcaabcaabcaa 이런 문자열이 나올 경우 문제 발생.
"""

T = int(input())

for n in range(T):
    str = input()
    # count = 0
    # check = True
    j = 0
    num = 0
    for i in range(1, len(str)):
        """
        -> index 범위 초과하는 경우 생각 못함
               if str[0] == str[i]:
                   for j in range(0, i):
                       if str[j] != str[i+j]:
                           check = False
                           break
                   if check:
                       sub_str = str[0:i]
                       print("#%d %d".format(n, len(sub_str)))
        """
        if str[i] == str[j]:
            j += 1
        else:
            j = 0

    num = len(str) - j
    print("#{} {}".format(n+1, len(str) - j))
