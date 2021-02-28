class Solution:
    def isValid(self, s: str) -> bool:
        data = {
            ']': '[',
            ')': '(',
            '}': '{',
        }

        st = []

        for i in s:
            if i not in data: # 키 값과 들어온 s 값 비교
                st.append(i) # ( { [
            elif not st or data[i] != st.pop():
                return False

        return len(st) == 0
