# 52ms / 14.2MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left_idx = 0
        dic = {}

        for right_idx, char in enumerate(s):
            if char in dic and left_idx <= dic[char]:  # Duplicated character
                left_idx = dic[char] + 1
            else:
                ans = max(ans, right_idx - left_idx + 1)
            dic[char] = right_idx

        return ans