def solution(board, moves):
    answer = 0
    dall_stack = []  # moves 해서 받아온 값 넣어두는 거
    for i in moves:  # 1 5 3 5 1 2 1 4
        for j in range(len(board)):  # 0--5
            if board[j][i - 1] > 0:  # 0보다 큰 값 중에서 출력
                # 젤 위의 값이랑 인형이랑 같은지 판별 (타입에러를 안내기 위해 0보다 클 때만)
                if len(dall_stack) > 0 and dall_stack[-1] == board[j][i - 1]:
                    dall_stack.pop()  # 맞으면 지운다.
                    answer += 2
                else:
                    dall_stack.append(board[j][i - 1])  # 스택에 인형을 추가함
                board[j][i - 1] = 0  # 뽑은 인형을 초기화함
                break
        # print(dall_stack)
    return answer
