# 첫번째 Brute Force O(n^3)
# max_sum = -int(1e9)
#
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         tmp = sum(nums[i:j+1])
#         if max_sum < tmp:
#             max_sum = tmp
# print(max_sum)


# 두번째 Optimization Brute Force O(n^2)
# max_sum = -int(1e9)
# for i in range(len(nums)):
#     value = 0
#     for j in range(i,len(nums)):
#         value += nums[j]
#         max_sum = max(max_sum,value)
# print(max_sum)


# 세번째 DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            print(nums[0])

        max_Sum = nums[0]

        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_Sum = max(max_Sum,nums[i])

        return max_Sum
