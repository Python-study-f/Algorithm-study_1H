class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        for ch in stones:
            if ch in jewels:
                cnt += 1
        return cnt

'''
1. 개념이므로 한줄코딩 안함
2. 이해안되면 톡주세영!
'''