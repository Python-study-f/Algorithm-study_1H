# Longest_Consecutive_Sequence 128


def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    nums = list(set(nums))
    nums.sort()

    prev = nums[0]
    ans = 1
    cnt = 1

    for i in range(1, len(nums)):
        if nums[i] == (prev + 1):
            cnt += 1
        else:
            cnt = 1
        ans = max(ans, cnt)
        prev = nums[i]

    return ans


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 0
#         nums = list(set(nums))
#         nums.sort()

#         prev = nums[0]
#         ans = 1
#         cnt = 1

#         for i in range(1, len(nums)):
#             if nums[i] == (prev + 1):
#                 cnt += 1
#             else:
#                 cnt = 1
#             ans = max(ans, cnt)
#             prev = nums[i]

#         return ans

print(longestConsecutive([100, 4, 200, 1, 3, 2]))
