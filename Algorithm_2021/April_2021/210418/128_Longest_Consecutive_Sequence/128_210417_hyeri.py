class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1        
        nums.sort()
        cnt = 0
        result = 0
        for i in range(len(nums)):
            if i == 0:
                cnt = 1
                continue
            if nums[i] == nums[i-1]:
                continue
            if nums[i]== nums[i-1] + 1:
                cnt += 1
            else:
                result = max(result, cnt)
                cnt = 1
                
        return max(result, cnt)
