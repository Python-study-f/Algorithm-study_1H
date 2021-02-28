class Solution:
    def maxProfit(self, prices: [int]) -> int:
        price= float('inf')
        ans=0
        for i in prices:
            price = min(price, i)
            ans = max(ans, i - price)

        return ans
