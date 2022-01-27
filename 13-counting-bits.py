"""
Given an integer n, return an array ans of length n + 1 such that 
for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""
# Brute force: o(n log n) solution
# def count_bits(n):
#   result = [0] * (n+1)
#   for i in range(n+1):
#       temp = i
#       count = 0
#       while temp != 0:
#           count += 1
#           temp = temp & (temp-1)
          
#       result[i] = count
  
#   return result

# Dynamic programming: O(n)
def count_bits(n):
  result = [0] * (n+1)
  offset = 1
  
  for i in range(1, n+1):
      if offset * 2 == i:
          offset = i
      result[i] = 1 + result[i-offset]
      
  return result

# print(count_bits(5)) # Expected output [0,1,1,2,1,2]
print(count_bits(8)) # Expected output [0,1,1,2,1,2,2,3,1]
