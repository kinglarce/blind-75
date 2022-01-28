"""
Problem: 
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""
# Dynamic Programming - O(n^2)
def length_of_LIS(nums):
  dp = [1]*len(nums)
  checker = 0
  base = 1
  
  while base < len(nums):
    if nums[checker] < nums[base]:
      dp[base] = max(dp[base],dp[checker]+1)
        
    checker += 1
    if checker >= base:
      base += 1
      checker = 0
  
  return max(dp)

def length_of_LIS(nums):
  dp = [1]*len(nums)
  for i in range(1, len(nums)):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)

  return max(dp)

# Binary search - O(nlogn)
def binary_search(sub, val):
  left, right = 0, len(sub)-1
  while(left <= right):
    mid = (left+right)//2
    
    if sub[mid] < val:
        left = mid + 1
    elif val < sub[mid]:
        right = mid - 1
    else:
        return mid
      
  return left

def length_of_LIS(nums):
  sub = []
  for num in nums:
    pos = binary_search(sub, num)
    if pos == len(sub):
      sub.append(num)
    else:
      sub[pos] = num

  return len(sub)
    
print(length_of_LIS([10,9,2,5,3,7])) # Expected 3 because its either [2,5,7] or [2,3,7]