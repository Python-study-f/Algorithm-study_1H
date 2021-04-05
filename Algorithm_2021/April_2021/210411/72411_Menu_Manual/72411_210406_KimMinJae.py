from itertools import combinations
def solution(orders, course):
    ans=[[2,[]] for _ in range(11)]
    for num in course:
        for customer in orders: # 이 고객에서 후보 추림
            
            for menus in combinations(list(customer), num): # 문제 1: 이거 리스트 아닌 객체라 그대로 변수에 저장하면 안됨
                cnt=0
                for L in orders: # 사람별로 후보 menus 다 있는 지 확인 # 문제 2: 7, 9 포문 순서 헷갈림
                    flag=True
                    for el in menus:
                        if el not in list(L):
                            flag=False
                            break
                    if flag:
                        cnt+=1

                if ans[num][0]<cnt:
                    ans[num][0]=cnt
                    ans[num][1]=[''.join(sorted(list(menus)))] # 문제 3: sorted 안함, 오름차순은 course만 돼있다..
                elif ans[num][0]==cnt:
                    ans[num][1]+=[''.join(sorted(list(menus)))]

    answer=[]
    for num in course:
        answer+=ans[num][1]


    return sorted(set(answer))

#print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))