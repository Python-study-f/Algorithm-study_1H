class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            if dict.get(i):
                dict[i] += 1
            else:
                dict[i] = 1
        sortedArr = []
        for key, val in dict.items():
            sortedArr.append((val,key))
        sortedArr.sort(reverse=True)
        ans = []
        for i in range(k):
            ans.append(sortedArr[i][1])
        return ans