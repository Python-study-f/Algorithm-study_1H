class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0
        nums.sort()

        # 큰수를 최대한 살려야한다.
        # 큰수를 살리기 위해서는 (max, max-1) 으로 묶어야한다
        for i in range(0 ,len(nums) ,2):
            result += nums[i]

        return result
        
