class Solution(object):
    def twoSum(self, nums, target):
        for idx, num in enumerate(nums):
            if target - num in nums:
                return idx, nums.index(target-num) # list.index() 는 () 안에 값을 list에 찾아서 인덱스로 반환

test = Solution()

nums = [2,7,11,15]
target = 9

print(Solution.twoSum(test,nums,target))