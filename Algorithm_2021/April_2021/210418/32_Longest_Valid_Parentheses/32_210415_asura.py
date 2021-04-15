class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st, cnt= [-1], 0  # 비어있을때, -1 로 반환하여 오류 index 넘어가는 거 오류 잡음

        if len(s) <= 1:
            return 0 

        for idx, c in enumerate(s):
            if c == "(":
                st.append(idx)
            else:
                st.pop()

                if not st:
                    st.append(idx)

                diff = idx - st[-1]
                cnt = max(cnt,diff)

        return cnt