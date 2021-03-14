from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        temp = Counter(nums)

        tt = temp.most_common(k)
       # print(tt)
        for i in range(k):
            ans.append(tt[i][0])

        return ans
