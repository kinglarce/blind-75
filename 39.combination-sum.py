"""
https://leetcode.com/problems/combination-sum/
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
"""
# Backtracking : T: O(n^t/m) t is target, m amount the minimal value of candidate,
# T: O(n^t/m)
def combination_sum(candidates, target) :
	result = []

	def backtrack(remaining, combination, start):
		if remaining == 0:
			# make deep copy of current combination
			result.append(list(combination))
			return
		elif remaining < 0: # exceeded the scope
			return 
		
		for i in range(start, len(candidates)):
			combination.append(candidates[i])
			# give the current number another chance, rather than moving on
			backtrack(remaining-candidates[i], combination, i)
			combination.pop()
					
	backtrack(target, [], 0)
	
	return result

print(combination_sum([2,3,6,7], 7))
				