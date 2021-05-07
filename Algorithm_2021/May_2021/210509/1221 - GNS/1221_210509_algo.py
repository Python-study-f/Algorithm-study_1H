T = int(input())
 
# 정렬용 알파벳
number_alpha = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
 
for tc in range(1,1+T):
 
    n = list(map(str,input().split()))
 
    # 무작위 숫자 리스트
    temp = list(map(str,input().split()))
 
    ans = []
 
    for i in range(10):
        for w in temp:
            if number_alpha[i] == w:
                ans.append(w)
 
    print(n[0])
    print(*ans)
