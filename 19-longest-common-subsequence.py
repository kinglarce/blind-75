"""
Problem:
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""
# Brute force - Recursive approach O(n*m), space of O(n*m)
def dp(text1, text2, i, j):
    if i == len(text1) or j == len(text2):
        return 0
    if text1[i] == text2[j]:
        return 1 + dp(text1, text2, i+1, j+1)
    else:
        return max(dp(text1,text2,i,j+1),dp(text1,text2,i+1,j))

def longest_common_subsequence(text1, text2):
    return dp(text1,text2,0,0)

#Dynamic programming 
def longest_common_subsequence(text1, text2):
    dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    for row in range(len(text1)-1,-1,-1):
        for col in range(len(text2)-1,-1,-1):
            if text2[col] == text1[row]:
                dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
            else:
                dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])

    return dp_grid[0][0]

print(longest_common_subsequence("ylqpejqbalahwr", "yrkzavgdmdgtqpg"))

