from collections import Counter
import string

low_lst = string.ascii_lowercase

s = "bcabc"

st = []
cnt = Counter(s)

# dic = {}
# for key in s:
#     if dic.get(key) is None:
#         dic[key] = 1
#     else:
#         dic[key] += 1
#
#   써보지 않았던 collection모듈 Counter 사용해봄. dictionary도 사용해보고 Counter 도 사용해봐야 할 거 같음.


for ch in s:
    cnt[ch] -= 1
