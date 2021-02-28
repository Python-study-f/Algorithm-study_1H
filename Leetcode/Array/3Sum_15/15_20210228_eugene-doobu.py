class Solution(object):
    def threeSum(self, nums):
        """
        https://leetcode.com/problems/3sum/
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        nums = sorted(nums)

        for i in range(len(nums)):
            #중복제거
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    #중복제거
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    #합이 0인 상태에서 left, right 둘중 하나만 움직이면 0이 나올리 없으므로 둘을 동시에 변경
                    left += 1
                    right -= 1

        return res
