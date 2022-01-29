# Approaches:
# 1. using 2 loops that check the arr and match them one by one - t: o(n2), s: o(1)
# 2. using sort, sort first the array then have a left index and right index runner
# that would increase left index if total of compared left & right is less than expected
# sum or decrease right index if total is more than expected sum until they find the right
# index for the total sum. - t: o(log(n)), s: o(1)
# 3. have a left index that set as a pivot while right index run until the end and compare 
# left and right index it match the total sum, when right index reach the end and still 
# nothing match the total sum, then left index moves forward by 1 - t: o(nlogn) s: o(1)
# 4 . using hashmap, record the subtracted difference in hashmap as a key then go through the array
# by subtracting the total sum with the current value, and if the difference is in the hashmap, then
# return the current value together with the subracted difference as this will total to 
# the total sum. - t: o(n), s: o(n)

# Problem:
# Given an array of integers, return the indices of two numbers such that they add up to the specific target

# input: [1,30,21,4,6,60], 81
# output: [21,60]
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

      