class Solution:
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        ans = []
        for i in range(0,n):
            ans.append(p)
    
            p = p * nums[i]
  
        p = 1
        for i in reversed(range(n)):
            ans[i] = ans[i] * p
            
            p = p * nums[i]
        return ans
