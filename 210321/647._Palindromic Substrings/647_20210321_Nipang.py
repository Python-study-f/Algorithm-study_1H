def solution(string):
    count = 0
    for a in range(len(string)+1):
        for b in range(len(string)+1):
            if b > a :
                str = list(string[a:b])
                if str == str[::-1]:
                    count +=1
    print("count is", count)


