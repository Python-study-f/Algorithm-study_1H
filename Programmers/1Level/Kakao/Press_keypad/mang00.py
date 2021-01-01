def find_func(keypad, i):  # 좌표 찾아주는 함수
    for x in range(4):  # keypad 세로 4
        for y in range(3):  # keypad 가로 3
            if keypad[x][y] == i:  # 좌표 값이랑 i 값이랑 같을 때
                return [x, y]  # 현재 좌표 반환


def solution(numbers, hand):
    answer = ''
    keypad = [  # 좌표를 비교하기 위한 2차원 배열
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]
    left = [3, 0]  # 왼쪽 좌표 초기화 시키기
    right = [3, 2]  # 오른쪽 좌표 초기화 시키기
    for i in numbers:
        if i in (3, 6, 9):
            answer += 'R'
            right = find_func(keypad, i)  # 현 좌표값 등록 [x,y]
        elif i in (1, 4, 7):
            answer += 'L'
            left = find_func(keypad, i)  # 현 좌표값 등록 [x,y]
        else:  # [2,5,8,0] 일 경우에
            now = find_func(keypad, i)  # 현 좌표값 등록 [x,y]
            # 왼쪽 좌표 x, y끼리 비교하기
            # 원래 int 했는데 에러뜨면서 python functions 가보니 abs()함수가 있어서 사용 (에러 아래 참고)
            # TypeError: 'builtin_function_or_method' object is not subscriptable 에러가 뜨면서 []연산자를 사용할 수 없다고 뜸
            # abs()함수 : 절대값을 반환 ex) abs(-11) = 11 이런 느낌
            left_comparison = abs(now[0] - left[0]) + abs(now[1] - left[1])
            # ex) 현재 7[2,1]을 가리키고 있는데 다음 숫자가 2[0,1]일 때 now[0] - left[0] = abs(2) / now[1] = left[1] = abs(0)
            # ex) left_comparison = 2
            # ex) 5 -> 8 / [1,2] -> [2,2] / -1 + 0 -1
            # 오른쪽 좌표 x, y끼리 비교하기
            right_comparison = abs(now[0] - right[0]) + abs(now[1] - right[1])
            # ex) 9[2,2]인데 2[0,1]일 때 right_comparison = 3
            if left_comparison > right_comparison:  # 만약 왼쪽 좌표가 오른쪽 좌표보다 크다면 가까운 오른쪽 값 불러오기
                right = now
                answer += 'R'
            elif left_comparison < right_comparison:  # 만약 오른쪽 좌표가 왼쪽 좌표보다 크다면 가까운 왼쪽 값 불러오기
                left = now
                answer += 'L'
            else:  # left_comparison == right_comparison
                if hand == 'right':  # 오른손이라면
                    right = now
                    answer += 'R'
                elif hand == 'left':  # 왼손이라면
                    left = now
                    answer += 'L'
    return answer
