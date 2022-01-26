"""
Problem: 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""
def three_sum(nums):
  nums.sort()
  result = []

  for i in range(len(nums)):
      cur_val = nums[i]
      if i > 0 and cur_val == nums[i-1]:
          continue
      left = i + 1
      right = len(nums)-1
      while left < right:
          total = cur_val + nums[left] + nums[right]
          if total == 0:
              result.append([cur_val, nums[left], nums[right]])
              left += 1
              # Move forward one more time until left 
              # value is not same a previous one
              while nums[left] == nums[left-1] and left < right:
                  left += 1
          elif total < 0:
              left += 1
          else:
              right -=1
              
  return result


# print(three_sum([-3,3,4,-3,1,2])) # Expected to equal 0
# print(three_sum([-1,0,1,2,-1,-4])) # Expected to equal 0 and [[-1,-1,2],[-1,0,1]]
print(three_sum([-2,0,0,2,2])) # Expected to equal 0 and [[-2,0,2],[-2,0,2]]