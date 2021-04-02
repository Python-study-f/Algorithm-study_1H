import sys
from itertools import combinations
L, C = map(int, sys.stdin.readline().split())
a = sorted(sys.stdin.readline().split())
lst = ['a', 'e', 'i', 'o', 'u']

for s in combinations(a, L):
    vowel, consonant = 0, 0
    for i in s:
        # if i in "aeiou":
        if i in lst:
            vowel += 1
        else:
            consonant += 1

    if vowel >= 1 and consonant >= 2:
    # if vowel >= 1 and vowel <= L -2:
        print(''.join(s))
