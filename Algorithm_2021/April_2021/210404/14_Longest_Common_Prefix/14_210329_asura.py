# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#
#         strs = sorted(strs, key=lambda x: len(x))
#
#         if len(strs) == 0:
#             return ""
#         else:
#             for i in range(len(strs[0])):
#                 for j in range(1, len(strs)):
#                     if strs[0][i] != strs[j][i]:
#                         return strs[0][:i]
#         return strs[0]



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=lambda x: len(x))
        st = []

        for x in zip(*strs):
            if len(set(x)) == 1:
                st.append(x[0])
            else:
                break

        return ''.join(st)