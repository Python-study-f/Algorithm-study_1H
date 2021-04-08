from itertools import combinations
from collections import Counter

def solution(orders, course):
    ans = []

    for crs in course:
        tmp = []
        for order in orders:
            if len(order) < crs:
                continue

            comb = combinations(sorted(order), crs)
            tmp += comb

        counter = Counter(tmp)
        if len(counter) and max(counter.values()) != 1:
            ans += [''.join(x) for x in counter if counter[x] == max(counter.values())]
    return sorted(ans)