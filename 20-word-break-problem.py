"""
Problem:
Given a string s and a dictionary of strings wordDict, return true if s can be 
segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""
# Brute force: Recursive: 
# Time complexity : O(2^n) Given a string of length nn, there are n + 1n+1 ways to split it into two parts. At each step, we have a choice: to split or not to split. 
# In the worse case, when all choices are to be checked, that results in O(2^n)
def helper(text, word_dict, start):
  if start == len(text):
    return True
  for end in range(start+1, len(text)+1):
    check_word = text[start:end]
    if check_word in word_dict and helper(text, word_dict, end):
      return True
  return False
# def word_break(text, word_dict):
#     return helper(text, word_dict, 0)

# Breath first search: T: O(n^3)
def word_break(text, word_dict):
  q = []
  visited = set()
  
  q.append(0)
  while q:
      start = q.pop(0)
      if start in visited:
          continue
      for end in range(start+1, len(text)+1):
          check_text = text[start:end]
          if check_text in word_dict:
              q.append(end)
              if end == len(text):
                  return True
      visited.add(start)
  return False
        
# Dynamic Programming: T: O(n^3)
def word_break_dp(text, word_dict):
  dp = [False]*(len(text)+1)
  dp[0] = True
  
  for i in range(1, len(text)+1):
    for j in range(i):
      check_text = text[j:i]
      if dp[j] and check_text in word_dict:
          dp[i] = True
          break
  
  return dp[len(text)]


print(word_break_dp("leetcode", ["leet","code"])) # Expected true
# print(word_break("catsandog", ["cats","dog","sand","and","cat"])) # Expected false

        
    
