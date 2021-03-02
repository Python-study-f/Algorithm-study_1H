from collections import Counter

# dic = {}
# for key in s:
#     if dic.get(key) is None:
#         dic[key] = 1
#     else:
#         dic[key] += 1
#
#   써보지 않았던 collection모듈 Counter 사용해봄. dictionary도 사용해보고 Counter 도 사용해봐야 할 거 같음.

from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st = []
        seen = set()
        cnt = Counter(s)

        for ch in s:
            cnt[ch] -= 1

            if ch in seen:
                continue
            while st and ch < st[-1] and cnt[st[-1]] > 0:
                seen.remove(st.pop())
            st.append(ch)
            seen.add(ch)

        return ''.join(st)

'''
1  문제 자체가 이해가 안됨. 그래서 일단 답지 보고 확인.
2. 스터디에서 논의하기 위해서 문제 정답은 구글링으로 찾아서 올림.
'''