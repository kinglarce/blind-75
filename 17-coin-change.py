"""
Problem:
You are given an integer array coins representing coins of different denominations and 
an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
"""
# Brute force - Greedy algorithm - Dont use
# def coin_change(coins, amount):
#   if amount < 1:
#       return 0
  
#   coins.sort()
#   temp_amount = 0
#   temp_count = 0
#   count = 0
#   runner = len(coins)-1
  
#   while runner >= 0:
#       if temp_amount == amount:
#           count = temp_count
#           break
#       elif (temp_amount+coins[runner]) <= amount:
#           temp_amount += coins[runner]
#           temp_count += 1
#       else:
#           runner -= 1
  
#   return count if count > 0 else -1

# Dynamic programming - Bottom up approach  
def coin_change(coins, amount):
    dp = [float('inf')] * (amount+1)
    dp[0] = 0 # compute amount 0 is always zero coin
    
    for coin in coins:
      for a in range(coin, amount+1):
        dp_prev_val = dp[a-coin]
        # the plus +1 comes from the coin being use
        # like incrementing +1 for each coin used
        dp_plus_1 = dp_prev_val+1
        dp_cur = dp[a]
        dp[a] = min(dp_cur, dp_plus_1)
    return dp[amount] if dp[amount] != float('inf') else -1

# dp = [0,1,1,2,2,3,3,4,4,5,5,6]
# Coin 2
# dp[a-coin] is the number it takes to achieve the amount of 'a'
# say 'a' is already 8 and 'coin' is 2
# dp[a-coin] will be dp[6] and its value is 3
# then we add +1 for the coin use to achieve 8 amount
# we then replace dp[8] with 4 from infinite
# eg. dp[8] = 4

# say 'a' is already 9 and 'coin' is still 2
# dp[a-coin] will be dp[7] and its value is 4
# then we add +1 for the coin use to achive 9 amount
# but as you can see, 5x 2 coin use to achieve 9 and it exceed the amount
# instead of only 9, we exceeded to 10 amount

# Coin 5
# say 'a' is already in 5 and 'coin' is 5
# dp[a-coin] will be 0 and add +1 for the coin use
# dp[5] = 1

# say 'a' is already in 6 and 'coin' is 5
# dp[a-coin] will be 1 and add +1 for the coin use 
# dp[6] = 2

# dp = [0,1,1,2,2,1,2,2,3,3,2,3]
# say 'a' is already in 10 and 'coin' is 5
# dp[a-coin] will be 1 and add +1 for the coin use
# so 2x 5 coin is use for the amount 10
# dp[10] = 2

# say 'a' is already in 11 and 'coin' is 5
# dp[a-coin] will 2(6th index) and add +1 for the coin use
# dp[11] = 3

# Top down - O(S * n) S is the amount and n is len(coins)
def get_min_coins(coins, amount, mem):
  if amount <= 0:
    return 0
  if amount in mem:
    return mem[amount]

  min_coins = float('inf')

  for coin in coins:
    if (amount - coin) <  0:
      break

    num_coins = get_min_coins(coins, amount - coin, mem) + 1
    min_coins = min(num_coins, min_coins)

  mem[amount] = min_coins

  return min_coins

def coin_change(coins, amount):
  coins.sort()
  min_coins = get_min_coins(coins, amount, {})
  
  if min_coins == float('inf'):
      return -1
  
  return min_coins

print(coin_change([1,2,5], 11)) # Expected 3
# print(coin_change([2],3)) # Expected -1
# print(coin_change([1],0)) # Expected 0
# print(coin_change([2,5,10,1], 27)) # Expected 4