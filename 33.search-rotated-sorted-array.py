"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
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

