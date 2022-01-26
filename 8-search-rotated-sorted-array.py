"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""

# Brute force: buggy with only 2 values(eg [3,1])
# def find_search(nums, target):
#   left, right = 0, len(nums)-1
#   while left < right :
#       mid = (left+right)//2
#       if nums[mid] > nums[right]:
#           left = mid+1
#       else:
#           right = mid 

#   pivot = left
#   dleft, dright = 0, len(nums)-1 
  
#   if target == nums[pivot]:
#       return pivot
#   elif target > nums[pivot]:
#       dleft = pivot
#   else:
#       dright = pivot
  
#   while dleft <= dright:
#       dmid = (dleft+dright)//2
      
#       if nums[dmid] == target:
#           return dmid
#       elif nums[dmid] < target:
#           dleft = dmid + 1
#       else:                
#           dright = dmid -1

#   return -1

# def find_search(nums, target):
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         mid = left + (right - left) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] >= nums[left]:
#             if target >= nums[left] and target < nums[mid]: # check if in between left half
#                 right = mid - 1
#             else: #  check if in between right half
#                 left = mid + 1
#         else:
#             if target <= nums[right] and target > nums[mid]: # check if in between right half
#                 left = mid + 1
#             else: # check if in between left half
#                 right = mid - 1
#     return -1

def find_search(nums, target):
    left, right = 0, len(nums)-1
    while left <= right :
        mid = (left+right)//2
        
        if target == nums[mid]:
            return mid
        
        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
                
    return -1
                
# print(find_search([4,5,6,7,0,1,2,3], 2))
print(find_search([4,5,6,7,0,1,2], 0))
# print(find_search([4,5,6,7,0,1,2], 3))
# print(find_search([1], 0))
# print(find_search([1,3],3))
# print(find_search([3,1],3))

