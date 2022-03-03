"""
https://leetcode.com/problems/house-robber/
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""
# def rob_from(nums, i, memo):
# 	if i >= len(nums):
# 		return 0
# 	if i in memo:
# 		return memo[i]
	
# 	current_house = nums[i]
# 	next_neighbor = rob_from(nums, i+1, memo)
# 	after_next_neighbor = rob_from(nums, i+2, memo)
# 	current_and_after_next_neighbor = after_next_neighbor+current_house
# 	res = max(next_neighbor, current_and_after_next_neighbor) 
# 	memo[i] = res
# 	return res

# def rob(nums): # Recursion: T: O(n), S: O(n) - Top Down
# 	return rob_from(nums, 0, {})



# def rob(nums): # Dynamic Programming - Bottom Up
# 	if not nums:
# 		return 0
	
# 	max_robbed_amount = [0]*(len(nums)+1)
# 	num_house = len(nums)
	
	
# 	max_robbed_amount[num_house] = 0
# 	max_robbed_amount[num_house-1]  = nums[num_house-1]
	
# 	for i in range(num_house-2, -1,-1):
# 		current_house = nums[i]
# 		next_rob_amount = max_robbed_amount[i+1]
# 		next_plus_one_rob_amout = max_robbed_amount[i+2]
# 		next_plus_one_with_current_rob_amount = next_plus_one_rob_amout+current_house
# 		max_robbed_amount[i] = max(
# 			next_rob_amount, 
# 			next_plus_one_with_current_rob_amount
# 		)
		
# 	return max_robbed_amount[0]

# def rob(nums): # Dynamic Programming(Optimize) - Bottom Up 
# 	if not nums:
# 		return 0
	
# 	num_house = len(nums)
	
# 	rob_next_plus_one = 0
# 	rob_next = nums[num_house - 1]
	
# 	# DP table calculations.
# 	for i in range(num_house - 2, -1, -1):
# 		rob_next_plus_one_with_current = rob_next_plus_one + nums[i]
# 		# Same as recursive solution.
# 		current = max(rob_next, rob_next_plus_one_with_current)
		
# 		# Update the variables
# 		rob_next_plus_one = rob_next
# 		rob_next = current
		
# 	return rob_next

def rob(nums): # Dynamic Programming(Optimize) - Top Down
        
	rob1, rob2 = 0,0
	
	for amount in nums:
		temp = max(amount+rob1, rob2)
		rob1 = rob2
		rob2 = temp
		
	return rob2

print(rob([100,200,300,100]))