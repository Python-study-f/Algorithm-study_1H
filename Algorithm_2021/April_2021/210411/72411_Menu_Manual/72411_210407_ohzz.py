# 메뉴 리뉴얼 72411
import collections


def comb(lst, n):
    res = []
    if n > len(lst):
        return res
    if n == 1:
        for i in lst:
            res.append([i])
    elif n > 1:
        for i in range(len(lst) - n + 1):
            for tmp in comb(lst[i + 1 :], n - 1):
                res.append([lst[i]] + tmp)
    return res


def solution(orders, course):
    answer = []
    for c in course:
        tmp = []
        for order in orders:
            for i in comb(order, c):
                i.sort()
                tmp.append("".join(i))
        tmp = collections.Counter(tmp).most_common()
        for key, value in tmp:
            if value >= 2 and tmp[0][1] == value:
                answer.append(key)
    answer.sort()
    return answer


# o = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# c = [2, 3, 4]

# print(solution(o, c))
