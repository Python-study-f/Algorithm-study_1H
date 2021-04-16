# 단어변환 43163

answer = 51


def solution(begin, target, words):
    checked = [0 for i in range(len(words))]

    def dfs(word, target, words, cnt):
        global answer

        if word == target:
            answer = min(cnt, answer)
        else:
            for i, value in enumerate(words):
                if checked[i] == 1:
                    continue
                tmp = 0
                for k in range(len(value)):
                    if value[k] != word[k]:
                        tmp += 1
                    if tmp > 2:
                        break
                if tmp == 1:
                    checked[i] = 1
                    dfs(value, target, words, cnt + 1)
                    checked[i] = 0

    dfs(begin, target, words, 0)

    if answer == 51:
        return 0

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
