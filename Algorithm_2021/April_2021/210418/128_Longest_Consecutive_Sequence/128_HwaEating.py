class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ndict = {}
        for num in nums:
            ndict[num] = 1
        keys = sorted(ndict.keys())
        ans = 0
        cnt = 0
        pre = -1e9
        print(keys)
        for i in keys:
            print(i)
            if pre == -1e9:
                cnt = 1
            elif i - pre == 1:
                cnt += 1
            else:
                ans = max(ans,cnt)
                cnt = 1
                
            pre = i
        ans = max(ans,cnt)
            
        return ans