class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        ans = 0
        l,r = 0,0
        n = len(s)
        while r < n:
            c = s[r]
            if dict.get(c):
                dict[c] += 1
            else: 
                dict[c] = 1
            while dict[c] > 1:
                dict[s[l]] -= 1
                l += 1
            ans = max(ans, r-l+1)
            r += 1
        return ans
            