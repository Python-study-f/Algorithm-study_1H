# Jump Game 2 45 LeetCode


def jump(nums):
    i = 0
    j = 1
    if len(nums) == 1:
        return 0
    for cnt in range(len(nums)):
        arr = []
        for k in range(i, j):
            arr.append(k + nums[k] + 1)
        i = j
        j = max(arr)
        if j >= len(nums):
            return cnt + 1


nums = [2, 3, 0, 1, 4]
print(jump(nums))
