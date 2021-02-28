class Solution:
    def reorderLogFiles(self, logs):
        letters, digits = [], []
        lens = len(logs)

        for i in range(lens):
            if logs[i].split()[1].isdigit():
                digits.append(logs[i])
            else:
                letters.append(logs[i])

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits


valid = Solution()
print(valid.reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act car"]))
