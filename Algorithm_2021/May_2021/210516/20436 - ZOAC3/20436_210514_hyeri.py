sl, sr = map(str, input().split())

key_left = {
    "z": (1, 1), "x": (1, 2), "c": (1, 3), "v": (1, 4), "a": (2, 1), "s": (2, 2), "d": (2, 3), "f": (2, 4), "g": (2, 5),
    "q": (3, 1), "w": (3, 2), "e": (3, 3), "r": (3, 4), "t": (3, 5)
}

key_right = {
    "b": (1, 5), "n": (1, 6), "m": (1, 7), "h": (2, 6), "j": (2, 7), "k": (2, 8), "l": (2, 9), "y": (3, 6), "u": (3, 7),
    "i": (3, 8), "o": (3, 9), "p": (3, 10)
}

st = input()

answer = 0
for ch in st:
    if ch in key_left:
        answer += abs(key_left[sl][0]-key_left[ch][0]) + abs(key_left[sl][1]-key_left[ch][1]) + 1
        sl = ch
    else:
        answer += abs(key_right[sr][0] - key_right[ch][0]) + abs(key_right[sr][1] - key_right[ch][1]) + 1
        sr = ch

print(answer)
