class Solution:    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(idx, num, visit):
            #print(num, visit)
            if num == target:
                ans.append(visit)
                return
            if num > target or idx >= len(candidates):
                return             
            dfs (idx, num + candidates[idx], visit + [candidates[idx]])
            if idx < len(candidates) :
                dfs(idx + 1, num, visit)

        dfs(0, 0, [])
        return ans
