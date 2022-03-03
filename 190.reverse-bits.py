"""
https://leetcode.com/problems/reverse-bits/
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
"""
# For debugging
def decimalToBinary(num, answer=[]):
  if num >= 1:
      answer.append(num % 2)
      decimalToBinary(num // 2, answer)
  return answer

"""
out = (out << 1)^(n & 1) adds last bit of n to out
n >>= 1 removes last bit from n.
Imagine number n = 11011010, and out = 0

out = 0, n = 1101101
out = 01, n = 110110
out = 010, n = 11011
out = 0101, n = 1101
out = 01011, n = 110
out = 010110, n = 11
out = 0101101, n = 1
out = 01011011, n = 0
"""

def reverse_bits(n):
        
  result = 0
  
  for i in range(32):
    shifted = result << 1
    invert_bit = n & 1
    result = shifted^invert_bit # invert 
    n = n>>1

  return result

# input 1101101
print(reverse_bits(91)) # Expected 01011011