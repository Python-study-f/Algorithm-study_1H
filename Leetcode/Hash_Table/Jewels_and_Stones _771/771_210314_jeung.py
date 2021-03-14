from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = list(stones)
        jewels = list(jewels)
        counted = Counter(stones)
        tot = 0

        for each_jewel in jewels:
            tot += counted[each_jewel]

        return tot
