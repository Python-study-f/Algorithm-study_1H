
from itertools import permutations

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# operator = list(map(int, input().split())) -> operator list로 할 시 for op in op_set에서 계산 처리할 때 복잡해짐.
add, sub, mul, div = map(int, input().split())
max_value, min_value = -1e9, 1e9

op_list = []
op_list += [1] * add
op_list += [2] * sub
op_list += [3] * mul
op_list += [4] * div

op_set = []
for num in list(permutations(op_list)):
    op_set.append(num)

op_set = list(set(op_set)) # 중복 제거

for op in op_set:
    answer = A[0]

    for i in range(N - 1):
        if op[i] == 1: # +
            answer += A[i + 1]
        elif op[i] == 2: # -
            answer -= A[i + 1]
        elif op[i] == 3: # *
            answer *= A[i + 1]
        elif op[i] == 4: # //
            if answer < 0: # 음수이면 +처리한 상태에서 나누고 다시 -를 씌움
                answer = -(-answer // A[i + 1])
            else:
                answer //= A[i + 1]

    min_value = min(min_value, answer)
    max_value = max(max_value, answer)

print(max_value)
print(min_value)
