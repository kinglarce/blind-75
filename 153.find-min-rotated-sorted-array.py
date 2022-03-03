"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
"""

def find_min(nums):
    left = 0
    right = len(nums)-1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[left]:
            left = mid + 1
        else:
            right = mid
            
    return nums[left]

find_min([3,4,5,1,2])
find_min([4,5,6,7,0,1,2])
find_min([11,13,15,17])