class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        for i in range(0,len(nums),2):
            ans+=(nums[i])
        #print(ans)
        return ans
