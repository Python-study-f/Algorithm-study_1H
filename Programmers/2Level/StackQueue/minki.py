def solution(priorities, location):
    answer = 0
    printCount = 0
    while len(priorities) != 0:
        first_item = priorities.pop(0)
        check = False
        for item in priorities:
            if item > first_item:
                check = True 
        if check:
            priorities.append(first_item)
            if location == 0:
                location += len(priorities)
        else:
            printCount += 1;
            if location == 0:
                answer = printCount
                break                
        location -= 1;
    return answer