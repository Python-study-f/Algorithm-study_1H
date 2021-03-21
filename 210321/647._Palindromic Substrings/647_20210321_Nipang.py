def solution(string):
    count = 0
    for a in range(len(string)+1):
        for b in range(len(string)+1):
            if b > a :
                str = list(string[a:b])
                if str == str[::-1]:
                    print(a)
                    print(b)
                    print("inverse is ",str[::-1])
                    print("true")
                    count +=1
    print("count is", count)
