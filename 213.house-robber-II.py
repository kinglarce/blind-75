"""
https://leetcode.com/problems/house-robber-ii/
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
"""
def robber(nums):
		rob1, rob2 = 0, 0
		
		for house in nums:
				temp = max(rob2, rob1+house)
				rob1 = rob2
				rob2 = temp
				
		return rob2

def rob(nums) -> int:
		if not len(nums):
				return 0
		if len(nums) == 1:
				return nums[0]
		return max(robber(nums[:-1]), robber(nums[1:]))
		
