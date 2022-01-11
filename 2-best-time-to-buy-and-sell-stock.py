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
def buy_sell_stocks(arr):
  max_profit = 0 
  left = 0
  right = left + 1
  while right < len(arr):
    current_value = arr[left]
    comparator_value = arr[right]
    if current_value < comparator_value:
      diff_value = comparator_value - current_value
      max_profit = max(diff_value, max_profit)
    else: 
      left = right
    right += 1

  return max_profit

  

print(buy_sell_stocks([7,1,5,3,6,4]))