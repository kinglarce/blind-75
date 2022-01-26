"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""
# Brute force: O(n)
# def max_area(height):
#   left, right = 0, 1
#   max_area = 0
  
#   while left < len(height)-1:
#       left_val = height[left]
#       right_val = height[right]
#       diff = right-left
#       area = diff * min(left_val, right_val)
#       max_area = max(max_area, area)
#       right += 1
#       if right >= len(height):
#           left += 1
#           right = left + 1
          
#   return max_area

def max_area(height):
  left, right = 0, len(height)-1
  max_area = 0
  
  while left < right:
    left_val = height[left]
    right_val = height[right]
    diff = right-left
    area = diff * min(left_val, right_val)
    max_area = max(max_area, area)
    if left_val <= right_val:
        left += 1
    else:
        right -= 1
          
  return max_area

print(max_area([1,8,6,2,5,4,8,3,7])) # Expected 49

