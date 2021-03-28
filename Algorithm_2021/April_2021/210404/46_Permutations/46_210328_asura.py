from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = permutations(nums,len(nums))

        return list(perm)
