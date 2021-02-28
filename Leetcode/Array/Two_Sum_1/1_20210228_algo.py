class Solution:
    def twoSum(self, nums, target):
        num_set = {}

        for index,num in enumerate(nums):
            if target-num in num_set:
                return [num_set[target-num],index]
            num_set[num]=index

        print(num_set)
