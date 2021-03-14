class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_t = 0
        for each_i in range(len(s)):
            # tmp_s = ''
            existing = []

            t = 0
            curr_s = s[each_i + t]
            while curr_s not in existing:
                existing.append(curr_s)
                t += 1
                if t + each_i >= len(s):
                    break

                curr_s = s[each_i+t]

            if t > max_t:
                max_t = t

        return max_t

solution = Solution()
print(solution.lengthOfLongestSubstring('abcabcbb'))
print(solution.lengthOfLongestSubstring('bbbbb'))
print(solution.lengthOfLongestSubstring('pwwkew'))