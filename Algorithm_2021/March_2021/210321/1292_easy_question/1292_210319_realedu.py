"""
1. 배경지식 - 수열
2. 문제 해결 기법 - 딱히 없는 듯
3. 구현 - lst에 수열을 넣는 방식 / 결과 구하는 방식
"""

# lst가 비어있는 상태에서 lst[i+j-1] = i는 안되는 것.
import sys
A, B = map(int, sys.stdin.readline().split())
lst = []
sum = 0
for i in range(1, 46):
    # for j in range(i):
        # lst[i+j-1] = i # list assignment index out of range
    lst += [i] * i
for i in range(A, B + 1):
    sum += lst[i - 1]
print(sum)

"""
결과 구하는 다른 방식
print(sum(lst[A-1:B]))
"""
