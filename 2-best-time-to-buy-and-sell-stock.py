# Approaches: 
# using left and right index, left set a base for comparing the running right index, if the current left value
# is greater than right value then change the left index to right index since its lower, if not then get 
# the difference by subtracting right to left value and compare it to existing max profit if its 
# greater, if it is then replace it and this goes on
# until the left reach the end - t: o(n), s: o(1)
# Problem:
# Say you have an array for which the i^th element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction(ie buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.
# Note: that you cannot sell a stock before you buy one.
# Example:
# input: [7,1,5,3,6,4]
# output: 5
# Explanation: Buy on day 2(price = 1) and sell on day 5(price = 6), profit = 6-1 = 5.
#           Not 7-1 = 6, as selling price need to be larger than buying price.
# Visualize: 
#   7 | *
#   6 |           *
#   5 |     *
#   4 |              *
#   3 |        *
#   2 |
#   1 |   *
#      ----------------
#
def buy_and_sell_stock(prices):
    max_profit = 0 
    left = 0
    right = left + 1
    while right < len(prices):
        if prices[left] < prices[right]:
            diff_value = prices[right] - prices[left]
            max_profit = max(diff_value, max_profit)
        else: 
            left = right
        right += 1
    return max_profit

def buy_and_sell_stock(prices):
  max_profit = 0
  for i  in range(len(prices) - 1):
      for j in range(i + 1, len(prices)):
          profit = prices[j] - prices[i]
          if profit > max_profit:
              max_profit = profit
              
  return max_profit
  
def buy_and_sell_stock(prices):
    min_price = float('inf')
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
        
    return max_profit 

print(buy_and_sell_stock([7,1,5,3,6,4]))