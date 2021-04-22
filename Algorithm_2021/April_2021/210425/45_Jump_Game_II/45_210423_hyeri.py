class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        dp = [len(nums)]*len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j == len(nums):
                    break
                dp[i + j] = min(dp[i] + 1, dp[i + j])
                
        return dp[len(nums)-1]
        
