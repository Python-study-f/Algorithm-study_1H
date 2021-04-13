class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        candidates.sort()

        def dfs(tot, lst, i):
            if tot == 0:
                ans.append(lst)
                return

            if i < len(candidates) and candidates[i] <= tot:
                dfs(tot - candidates[i], lst + [candidates[i]], i)
                dfs(tot, lst, i + 1)

        dfs(target, [], 0)
        return ans
# 리스트에서 append의 반환값은 리스트로 나오는 것이 아닌것을 다시 깨우쳤당..
# DP가 아니라 DFS로 풀면 될 거 같은 느낌의 문제다.
