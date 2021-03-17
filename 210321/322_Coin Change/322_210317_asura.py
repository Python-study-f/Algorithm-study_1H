class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = int(1e9)
        dp = [INF] * (amount+1)
        dp[0] = 0

        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                if dp[j-coins[i]] != INF:
                    dp[j] = min(dp[j],dp[j-coins[i]] + 1)

        if dp[amount] == INF:
            return -1

        else:
            return dp[amount]