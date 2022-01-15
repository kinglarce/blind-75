# Problem:
# Given an interger array `nums`, find the contiguous subarray (containing at least our number)
# which has the largest sum and return its sum.
 
# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6

# Approach:
# (Brute) - Compute every sub array using left index as a base while right index run through the list and get the contiguous max number 
# by summing up each and comparing to right index value then record after wards. - t: o(n2), s: o(1)
# this is like 
# for(i=0...)
#   for(i=j...)
# but here im just using while loop
# def max_subarray(arr):
#   left = 0
#   right = 0
#   max_num = 0
#   record_indices = []
#   while left < len(arr)-1:
#     left_value = arr[left]

#     # move the right index next to left index then set the base max num and current/prev total for comparison
#     right = left + 1 # placing right index
#     temp_max_num = left_value
#     currently_hold_max_right_index = right
#     compared_total_sum = left_value
    
#     # right index run through the list and compare each sum value then grab new max subarray
#     while right < len(arr):
#       right_value = arr[right]
#       compared_total_sum = compared_total_sum + right_value
#       if compared_total_sum > temp_max_num:
#         temp_max_num = max(compared_total_sum, temp_max_num)
#         currently_hold_max_right_index = right
#       right += 1

#     # record the indices max subarray sum and grab the max number
#     record_indices.append([left, currently_hold_max_right_index, temp_max_num])
#     max_num = max(temp_max_num, max_num)
#     left += 1

#   return max_num

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