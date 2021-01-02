def solution(numbers, hand):
    result = ""
    right_now = '#'
    left_now = '*'
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              '*': (3, 0), 0: (3, 1), '#': (3, 2),
             }
    for number in numbers:                          # [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	반복
        # 왼쪽 키패드
        if number == 1 or number == 4 or number == 7:
            result += "L"
            left_now = number
        # 오른쪽 키패드
        elif number == 3 or number == 6 or number == 9:
            result += "R"
            right_now = number
        # 가운데 키패드
        else:
            # 거리 : 수직 거리 + 수평 거리
            left_distance = abs(keypad[left_now][0] - keypad[number][0]) + abs(keypad[left_now][1] - keypad[number][1])
            right_distance = abs(keypad[right_now][0] - keypad[number][0]) + abs(keypad[right_now][1] - keypad[number][1])
            
            # 오른쪽 손가락으로 누름
            if left_distance > right_distance:
                result += 'R'
                right_now = number
            # 왼쪽으로 누름
            elif left_distance < right_distance:
                result += 'L'
                left_now = number
            # 길이가 같을 때
            else:
                if hand == 'right':
                    result += 'R'
                    right_now = number
                elif hand == 'left':
                    result += 'L'
                    left_now = number
    
    return result
