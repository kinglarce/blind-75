"""
https://leetcode.com/problems/missing-number/
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
"""
# def missing_number(nums):
#   total_range_sum = sum(range(0, len(nums)+1))
#   missing_nums_sum = sum(nums)
#   result = total_range_sum-missing_nums_sum
#   return result

# def missing_number(nums):
#   len_nums = len(nums)
#   divided_len_nums = (len(nums)+1)
#   expected_sum = len_nums*divided_len_nums//2
#   actual_sum = sum(nums)
#   return expected_sum - actual_sum  

def missing_number(nums):
  missing = len(nums)
  for i, num in enumerate(nums):
      missing ^= i ^ num
  return missing

print(missing_number([0,1])) # Expected 2
print(missing_number([9,6,4,2,3,5,7,0,1])) # Expected 8
