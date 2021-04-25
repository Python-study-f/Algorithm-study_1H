class Solution:
    def jump(self, nums: List[int]) -> int:
        
        target = len(nums) - 1 
        count = 0 
        
        while target > 0: 
            index = 0 
            
            while nums[index] + index < target:
                index += 1 
            
            target = index 
            
            count += 1 
        
        return count 
