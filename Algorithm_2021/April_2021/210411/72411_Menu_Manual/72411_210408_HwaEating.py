def combinations(s,length,start=0,pick=[]):
    global combs, sale
    if length == len(pick):
        pick.sort()
        combs[length].add(''.join(pick))
        return
    
    for i in range(start,len(s)):
        combinations(s,length,i+1, pick+[s[i]])

def solution(orders, course):
    global combs, sale, ans
    sale = {}
    ans = {}
    for order in orders:
        for menu in order:
            if not sale.get(menu):
                sale[menu] = 0
            sale[menu] += 1
    
    combs = {}
    for cs in course:
        combs[cs] = set()
        ans[cs] = {}
        for order in orders:

            combinations(order, cs)

    answer = []

    for cs in course:
        for menu in combs[cs]:
            score = 0
            for order in orders:
                if set(menu)&set(order) == set(menu):
                    score += 1
            if score > 1:
                if not ans[cs].get(score):
                    ans[cs][score] = []
                ans[cs][score].append(menu)

    for cs in course:
        if ans.get(cs):
            mx = max(list(ans[cs].keys()))
            answer.extend(ans[cs][mx])
    answer.sort()

    return answer