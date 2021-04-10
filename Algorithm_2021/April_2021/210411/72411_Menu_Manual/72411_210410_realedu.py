
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        temp = []
        for order in orders:
            comb = combinations(sorted(order), c)
            temp += comb
        count = Counter(temp)
        # print(count.keys())
        
        # 주문 조합이 없거나 (case 3 - Counter()) / 해당 조합을 주문한 사람이 2명 이상일 때 처리
        if len(count) != 0 and max(count.values()) >= 2:
            for i in count.keys():
                if count[i] == max(count.values()):
                    answer.append(''.join(i))
    
    answer.sort()
    return answer
