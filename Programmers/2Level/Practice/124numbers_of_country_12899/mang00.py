def solution(n):
    number_basket = ['1', '2', '4']
    share = (n - 1) // 3  # 몫
    remainder = (n - 1) % 3  # 나머지
    if n <= 3:
        return number_basket[n - 1]
    else:
        return solution(share) + number_basket[remainder]