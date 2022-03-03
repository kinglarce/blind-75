# https://leetcode.com/problems/contains-duplicate/
# Input: [1,2,3,1]
# Output: true

def contains_duplicate(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

def contains_duplicate(nums):
    nums_set = list(set(nums))
    return not (len(nums_set) == len(nums))

def contains_duplicate(nums):
    uniq_nums = set()
    for num in nums:
        if num in uniq_nums:
            return True
        uniq_nums.add(num)
    return False

print(contains_duplicate([1,2,3,4,1]))
# print(contains_duplicate([1,2,3,4]))
# print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))

