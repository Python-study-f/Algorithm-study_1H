

def solution(d, budget):
    result = 0
    d.sort()
    price = 0
    for i in d:
        if price + i <= budget:
            price = price + i
            result += 1
        else:
            break
    return result
