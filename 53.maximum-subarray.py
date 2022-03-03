# https://leetcode.com/problems/maximum-subarray/
# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6

# Approach: - They say this is similiar to "Sliding Window" problem
# Check the current index value and current temporary sum, if its negative then reset the temporary sum, 
# if not then check whether the temporary sum is bigger than the max number, and if so, then replace it.
# - t: o(n), s: o(s)
# remove negetive prefix 
def max_subarray(arr):
  max_num = 0
  left = 0
  temp_sum = 0
  while left < len(arr):
    temp_sum = temp_sum + arr[left]
    if temp_sum < 0 and arr[left] < 0:
      temp_sum = 0
    else:
      max_num = max(temp_sum, max_num)
    left += 1
  return max_num

# Another approach but same idea as above
def max_subarray(arr):
  max_num = arr[0]
  current_sum = 0
  for num in arr:
    if current_sum < 0:
      current_sum = 0
    current_sum += num
    max_num = max(current_sum, max_num)
  return max_num

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))