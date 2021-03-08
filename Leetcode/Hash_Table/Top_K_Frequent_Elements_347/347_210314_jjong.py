class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        lst = Counter(nums)

        lst_ = lst.most_common(k)

        for i in range(k):
            ans.append(lst_[i][0])

        return ans