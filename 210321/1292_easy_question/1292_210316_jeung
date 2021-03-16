def solution(n1, n2):
    count = 0
    element = 0

    while n1 - count > 0:
        element += 1
        count += element

    tot = element * (count - n1 + 1)

    while n2 - count > 0:
        element += 1
        count += element
        tot += element * element

    tot -= element * (count - n2)

    return tot
