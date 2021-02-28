class Solution:
    def reorderLogFiles(self, logs):
        letters, digits = [], []

        for i in range(len(logs)):
            if logs[i].split()[1].isdigit():
                digits.append(logs[i])
            else:
                letters.append(logs[i])

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
