# https://leetcode.com/problems/two-sum/
# Input: [1,30,21,4,6,60], 81
# Output: [21,60]
def two_sum(nums, target):
    uniq = {}
    for i in range(len(nums)): 
        num_diff = abs(target-nums[i])
        if not num_diff in uniq:
            uniq[nums[i]] = True
        else:
            return [nums[i], num_diff]
    return False

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i]+nums[j]) == target:
                return [i, j]

def two_sum(nums, target):
    left, right = 0, len(nums)-1
    while left < right:
        total = nums[left]+nums[right]
        if total == target:
            return [left+1, right+1]
        elif total < target:
            left += 1
        else:
            right -= 1
    return -1

print(two_sum([1,30,21,4,6,60], 81))

      