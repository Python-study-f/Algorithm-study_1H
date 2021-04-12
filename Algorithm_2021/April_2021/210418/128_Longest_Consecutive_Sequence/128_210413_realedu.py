"""
효율이 너무 쓰레기
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        # print(nums)
        
        result = 0
        # 연속적인 숫자들만 찾는 방법?
        for i in nums:
            if i-1 not in nums:
                cur_value = i
                length_cur_value = 0
                
                while i in nums:
                    i += 1
                    length_cur_value += 1
                    result = max(result, length_cur_value)
        
        return result
