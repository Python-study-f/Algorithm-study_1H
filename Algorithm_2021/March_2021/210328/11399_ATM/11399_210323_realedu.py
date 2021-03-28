

"""
브루트포스 -> O(1000!) ㅈㄴ 큼
그리디
- list에 대해 오름차순 정렬 후 sum에 합 더하기
- O(1000 * 1000) -> 대략 100만번 / 1초안에 가능
"""

import sys

input = sys.stdin.readline
N = int(input())

# lst = map(int, input().split())
# lst = list[map(int, input().split())] -> Builtin 'list' cannot be parameterized directly
lst = list(map(int, input().split()))
lst.sort()
sum = 0
for i in range(N):
    for j in range(i + 1):
        sum += lst[j]

print(sum)
