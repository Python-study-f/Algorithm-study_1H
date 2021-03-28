def is_palindromic(s):
    if s == s[::-1]:
        return True
    else:
        return False


class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        start = 0
        end = 1
        tot_count = 0
        while start < length:
            sub_string = s[start:end]
            palindromic_flag = is_palindromic(sub_string)
            if palindromic_flag:
                tot_count += 1
            end += 1

            if end > length:
                start += 1
                end = start + 1

        return tot_count
