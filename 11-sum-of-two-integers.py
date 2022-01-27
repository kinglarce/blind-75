"""
Problem:
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
"""

def get_sum(a, b):
  x, y = abs(a), abs(b)
  # ensure that abs(a) >= abs(b)
  if x < y:
      return get_sum(b, a)
  
  # abs(a) >= abs(b) --> 
  # a determines the sign
  sign = 1 if a > 0 else -1
  multi = a * b
  
  if multi >= 0:
      # sum of two positive integers x + y
      # where x > y
      while y:
          answer = x ^ y
          carry = (x & y) << 1
          x, y = answer, carry
  else:
      # difference of two integers x - y
      # where x > y
      while y:
          answer = x ^ y
          borrow = ((~x) & y) << 1
          x, y = answer, borrow
  
  return x * sign

get_sum(-1, 1)
get_sum(2, 3)