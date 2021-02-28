class Solution:
    def productExceptSelf(self, nums):
        total = 1
        result = []
        lens = len(nums)

        for i in range(lens):
            result.append(total)
            total *= nums[i]
        total = 1

        for j in range(lens - 1, -1, -1):  # 3, -1까지 -1씩
            result[j] *= total
            total *= nums[j]
        return result


valid = Solution()
print(valid.productExceptSelf([1, 2, 3, 4]))
