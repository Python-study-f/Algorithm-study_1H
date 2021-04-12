# 1. Brute_Force 기법
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))

        if len(nums) == 1:
            return 1

        cnt = 1
        ans = 0

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
        return ans

'''

# 2. Hash_Table 을 이용한 방법

'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        nums_hash = {}
        ans = 1

        # 어차피 set 떄려서 하나씩밖에 없음.
        for num in nums:
            nums_hash[num] = 1

        for i in range(1, len(nums)):
            if nums[i] - 1 not in nums_hash:
                nums_hash[nums[i] - 1] = 0
            
            nums_hash[nums[i]] = nums_hash[nums[i] - 1] + 1
            ans = max(ans,nums_hash[nums[i]])

        return ans
'''
