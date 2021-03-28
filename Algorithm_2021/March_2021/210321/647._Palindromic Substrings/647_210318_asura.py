def is_palindromic(s):
    if s == s[::-1]:
        return True
    else:
        return False


class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0

        for i in range(len(s) + 1):
            for j in range(1, len(s) + 1):
                if is_palindromic(s[i:j]):
                    if len(s[i:j]) != 0:
                        cnt += 1

        return cnt