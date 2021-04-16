class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if len(nums) == 1:
            return 1
        cnt = 1
        answer = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer, cnt)
        return answer
