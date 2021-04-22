# 36ms, 45.40%

class Solution: # O(N^2)
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 1

        dp = [int(1e9)] * len(nums)
        dp[0], dp[1] = 0, 1

        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] + j >= i and dp[j] != int(1e9):  # 조건식 만드는데 한참 오래 걸림.. 점화식 문제가 아니였던 거 같음 ㅠㅠ..
                    dp[i] = min(dp[j] + 1, dp[i])

        return dp[-1]