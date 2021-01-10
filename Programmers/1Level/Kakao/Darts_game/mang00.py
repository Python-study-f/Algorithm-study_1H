def solution(dartResult):
    total = []
    list_dart = list(dartResult)
    basket = []
    for i in range(len(list_dart)):
        if list_dart[i] == '1' and list_dart[i + 1] == '0':
            basket.append('10')
        elif list_dart[i] == '0' and list_dart[i - 1] == '1':
            continue
        else:
            basket.append(list_dart[i])
    for i in range(1, len(basket)):
        if basket[i] == 'S':
            total.append(int(basket[i - 1]) ** 1)
        elif basket[i] == 'D':
            total.append(int(basket[i - 1]) ** 2)
        elif basket[i] == 'T':
            total.append(int(basket[i - 1]) ** 3)

        if basket[i] == '*':
            if len(total) >= 2:
                total[-1] = total[-1] * 2
                total[-2] = total[-2] * 2
            else:
                total[-1] = total[-1] * 2
        elif basket[i] == '#':
            total[-1] = total[-1] * (-1)
    return sum(total)