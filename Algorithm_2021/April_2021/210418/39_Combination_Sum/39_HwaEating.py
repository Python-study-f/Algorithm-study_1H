class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        global ans
        def sums(candi, target, rs=0, li=[]):
            global ans
            if rs == target:
                ans.append(li)
                return
            
            for i in candi:
                if not li:
                    if rs+i <= target:
                        sums(candi, target,rs+i, li+[i])
                elif li[-1] <= i:
                    if rs+i <= target:
                        sums(candi,target,rs+i,li+[i])
        
        candidates.sort()
        ans = []
        sums(candidates,target)
        return ans