class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        c = len(coins)
        m = amount
        ks = [[1e9]*(m+1) for _ in range(c+1)]
        
        for i in range(c+1):
            ks[i][0] = 0
            
        for i in range(1,c+1):
            val = coins[i-1]
            for j in range(1,m+1):
                if val > j:
                    ks[i][j] = ks[i-1][j]
                else:
                    ks[i][j] = min(ks[i][j-val]+1, ks[i-1][j])
        if ks[c][m] < 1e9:
            return ks[c][m]
        else:
            return -1
        