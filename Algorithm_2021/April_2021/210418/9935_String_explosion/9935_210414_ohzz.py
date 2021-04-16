import sys

string = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()
word = list(word)

res = []

for i in string:
    res.append(i)
    if word == res[-len(word) :]:
        del res[-len(word) :]

if len(res) == 0:
    print("FRULA")
else:
    print("".join(res))

# string = sys.stdin.readline().rstrip()
# word = sys.stdin.readline().rstrip()

# tmp = string.split(word)
# while True:
#     if len(tmp) == 1:
#         tmp = "".join(tmp)
#         break
#     tmp = "".join(tmp)
#     tmp = tmp.split(word)

# if tmp == "":
#     print("FRULA")
# else:
#     print(tmp)
