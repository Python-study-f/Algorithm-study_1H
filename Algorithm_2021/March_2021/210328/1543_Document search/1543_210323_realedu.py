

"""
1번째 문자열 - 2번째 문자열한 길이만큼 index를 돌면서
(index, index + 2번째 문자열길이)만큼 탐색을 한다.
맞으면 count + 1과 함께 index의 값을 2번째 문자열길이만큼 최신화하고
틀리면 index += 1만 한다.
"""

import sys

# sys를 이용해서는 안되는가?
# string_1st = sys.stdin.readline().split()
# string_2nd = sys.stdin.readline().split()

string_1st = input()
string_2nd = input()

count = 0
i = 0

while i <= len(string_1st) - len(string_2nd):
    if string_1st[i:i+len(string_2nd)] == string_2nd:
        count += 1
        i += len(string_2nd)
    else:
        i += 1

print(count)
