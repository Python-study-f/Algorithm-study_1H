ans = int(1e9)

def solution(begin, target, words):
    visited = [False] * len(words)

    def dfs(start, end, cnt):
        global ans

        if start == end:
            ans = min(cnt, ans)
            return
        else:
            for idx, word in enumerate(words):
                if visited[idx]:
                    continue

                count = 0

                for i in range(len(word)):  # 몇개가 틀리고 맞는지 체크
                    if start[i] != word[i]:
                        count += 1
                else:
                    if count == 1:
                        visited[idx] = True
                        dfs(word, end, cnt + 1)
                        visited[idx] = False

    if target not in words:
        return 0
    else:
        dfs(begin, target, 0)
        return ans
