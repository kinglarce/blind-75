"""
https://leetcode.com/problems/climbing-stairs/
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
# This is like a fibanocci
# Bottom up approach
# def climb_stairs(n, memo={}):
#   if n <= 2:
#       return n
#   if n not in memo:
#       memo[n] = climb_stairs(n-1, memo) + climb_stairs(n-2, memo)
  
#   return memo[n]

# Top down approach with O(1) space
def climb_stairs(n):
  if n <= 2:
      return n
  one, two = 1, 2
  for _ in range(3, n+1):
      one, two = two, one+two
      
  return two
    
print(climb_stairs(5)) # Expected 8