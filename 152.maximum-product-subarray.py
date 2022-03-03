# https://leetcode.com/problems/maximum-product-subarray/
# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# Brute force
def max_product(nums):
  if len(nums) == 0:
      return 0

  result = max(nums)

  for i in range(len(nums)):
      accu = 1
      for j in range(i, len(nums)):
          accu *= nums[j]
          result = max(result, accu)

  return result

def max_product(nums):
  result = max(nums)
  min_so_far = 1
  max_so_far = 1

  for num in nums:
    if num == 0:
      min_so_far = 1
      max_so_far = 1
      continue

    # this variable just hold the current max prod value since its 
    # gonna be replaced later
    temp_max_holder = max_so_far * num
    max_so_far = max(num * max_so_far, num * min_so_far, num)
    min_so_far = min(temp_max_holder, num * min_so_far, num)

    result = max(max_so_far, result)

  return result



        
max_product([2,3,-2,4]) # Expected 6
max_product([-2]) # Expected -2
max_product([-3,-1,-1]) # Expected 3