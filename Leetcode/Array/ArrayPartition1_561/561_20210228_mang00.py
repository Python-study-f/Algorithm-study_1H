class Solution:
    def arrayPairSum(self, nums):
        # 첫번째 방법
        # sum = 0
        # basket = []
        # nums.sort()
        #
        # for n in nums:
        #     basket.append(n)
        #     if len(basket) == 2:
        #         sum += min(basket)
        #         basket = []
        #
        # return sum

        total = 0
        nums.sort()

        for i, j in enumerate(nums):
            if i % 2 == 0:
                total += j

        return total


valid = Solution()
print(valid.arrayPairSum([6, 2, 6, 5, 1, 2]))
