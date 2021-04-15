# 19.74% 83.95% slow
def longestConsecutive(nums):
    nums.sort()
    n= len(nums)
    if not n:
        return 0
    mx=1
    tmp=1
    for i in range(n-1):
        if nums[i]==nums[i+1]:
            continue
        if nums[i]+1==nums[i+1]:
            tmp+=1
        else:
            mx=max(mx,tmp)
            tmp=1
    return max(mx,tmp)

print(longestConsecutive([1,2,3,7,8,9,10]))


'''
이게 조금 더 빠른 이유는?
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n= len(nums)
        if not n:
            return 0
        mx=1
        tmp=1
        for a, b in zip(nums,nums[1:]+[-1e9]): # 오른쪽껄더함
            if a==b:
                continue
            if a+1==b:
                tmp+=1
            else:
                mx=max(mx,tmp)
                tmp=1
        return mx
'''