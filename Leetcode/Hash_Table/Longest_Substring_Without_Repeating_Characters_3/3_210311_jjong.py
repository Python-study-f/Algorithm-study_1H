# 52ms / 14.2MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left_cursor = 0
        used = {}

        for right_cursor, char in enumerate(s):
            if char in used and left_cursor <= used[char]:  # Duplicated character
                left_cursor = used[char] + 1
            else:
                ans = max(ans, right_cursor - left_cursor + 1)
            used[char] = right_cursor

        return ans