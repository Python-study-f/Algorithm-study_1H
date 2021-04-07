from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer=[]
    for i in course:
        dict=[]
        for j in orders:
            tt=sorted(j)
            for s in combinations(tt,i):
                dict.append(''.join(s))
        dict= Counter(dict).most_common()
        print(dict)
        maxcnt=dict[0][1]
        for x in dict:
            if x[1] == maxcnt and maxcnt >=2:
                answer.append(x[0])
    return sorted(answer)
