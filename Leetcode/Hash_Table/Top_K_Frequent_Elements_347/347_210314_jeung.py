from collections import defaultdict
class Solution:
    def topKFrequent(self, nums, k):
        count_dict = defaultdict(int)
        for i in nums:
            count_dict[i] += 1
        return [each_key for each_key, v in sorted(count_dict.items(), key=lambda item: item[1])][::-1][:k]

