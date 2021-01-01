def solution(s, n):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    alpha2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
    answer2 = []
    for i in list(s):
        if 64 < ord(i) < 91:  # 대문자
            answer2 += alpha2[(ord(i) + n - ord('A')) % len(alpha2)]
        elif 96 < ord(i) < 123:  # 소문자
            # 'z', 2 => 122 + 2 - 97 => 27 % 26 => 1 => [1] = 'b'
            answer2 += alpha[(ord(i) + n - ord('a')) % len(alpha)]
        else:
            answer2 += i
    return ''.join(answer2)
