class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        lst = []
        nums.sort()

        for start in range(len(nums)):
            if start > 0 and nums[start] == nums[start - 1]: # 한번 고정값으로 썼으면 넘어가
                continue

            left, right = start + 1, len(nums) - 1  # 인덱스를 나타내는거야
            while left < right:
                sums = nums[start] + nums[left] + nums[right]
y
                if sums < 0:
                    left = left + 1
                elif sums > 0:
                    right = right - 1
                else:
                    lst.append(sorted([nums[start], nums[left], nums[right]]))

                    left += 1
                    right -= 1

        RET = list(set(map(tuple, lst)))
        return RET

'''
1. 2-point로 풀었음.
2. 마지막 else 채우는데 대부분 시간 허비함. 어디서 무한루프 도는지 모르고 있었음.
3. brute-force 로 O(n^3) 해봤는데 1억 넘어서 패스
'''