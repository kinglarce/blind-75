"""
https://leetcode.com/problems/number-of-1-bits/
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
"""
# Just a debugging function for checking the binary of the number
def decimalToBinary(num):
  if num >= 1:
      decimalToBinary(num // 2)
      print(num % 2)

# Brute force: O(1)
def count_bits(n):
  print("curren ; ", n, " - ", decimalToBinary(n))
  print("shifted: ", n>>1, " - ", decimalToBinary(n>>1))

  result = 0
  while n:
      result += n % 2 # This give 1 or 0 and just add up to result
      n = n>>1
      
  return result

# Better solution: O(1)
def count_bits(n):
  result = 0
        
  while n != 0:
      result += 1
      n = n & (n-1)
      
  return result

print(count_bits(11)) # Expected output 3