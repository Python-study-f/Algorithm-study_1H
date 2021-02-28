class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        111-
        22-2
        3-33
        -444
        ====
        6812
          24
        """
        length = len(nums)
        result = [1] * length

        weight = 1
        for i in range(length):
          result[i] = result[i] * weight
          weight *= nums[i]

        weight = 1
        for j in range(length-1, -1, -1):
          result[j] = result[j] * weight
          weight *= nums[j]

        return result
