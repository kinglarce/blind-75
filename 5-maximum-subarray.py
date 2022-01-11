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

def max_subarray(arr):
  pass

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))