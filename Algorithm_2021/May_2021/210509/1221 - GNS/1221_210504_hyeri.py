T = int(input())
num = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
for test_case in range(1, T+1):
    tmp = input()
    sent = list(input().split())
    print("#{} ".format(test_case))

    for n in sent:
        if n in num:                                    # 딕셔너리에 key 값이 있을 경우
            num[n] += 1                                 # 갯수 증가
            
    for key, value in num.items():
        print("{0}".format(key + ' ') * value, end="")  # 차레로 갯수 출력
        num[key] = 0                                    # 초기화
