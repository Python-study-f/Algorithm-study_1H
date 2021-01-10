def solution(board, moves):
    answer = 0
    basket_list = []
    for i in range(len(moves)):                    # 1 -> 5 -> 3 -> 5 -> 1 -> ..
        for j in board:                # board 하나씩 돌려봄
            if j[moves[i]-1] > 0:
                basket_list.append(j.pop(moves[i]-1))
                j.insert((moves[i]-1), 0)
                break
        if len(basket_list) >= 2 and basket_list[len(basket_list)-1] == basket_list[len(basket_list) -2]:
            basket_list.pop(-1)
            basket_list.pop(-1)
            answer += 2

    return answer
