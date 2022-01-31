# Approaches:
# 1. using hastmaps, where we record the number that we already passed and if it exiss in the hashmaps,
# then it duplicate - t: o(n), s: o(n)
# 2. can using left inde and right index, right is the runner to check the value of left if it exists and 
# increment left index if it not until left reach the end - t: o(n), s: o(1)
# 3. or just use, "in" operator in python which check if value exist in the array

# Problem:
# Given an interger array, return True if any value appears AT LEAST TWICE in the array,
# and return False if every element is distinct.

# input: [1,2,3,1]
# output: true

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

