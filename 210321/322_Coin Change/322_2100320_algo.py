class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        temp = [float('inf')] * (amount + 1)
        temp[0] = 0
        
        for c in coins:
            for a in range(len(temp)):
                if c <= a:
                    temp[a] = min(temp[a-c]+1, temp[a])
                    
      #  print(temp)
        if temp[amount] == float('inf'):
            return -1
        return temp[amount]  
