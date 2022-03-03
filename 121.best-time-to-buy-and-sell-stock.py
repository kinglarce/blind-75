"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2(price = 1) and sell on day 5(price = 6), profit = 6-1 = 5.
Not 7-1 = 6, as selling price need to be larger than buying price.
# Visualize: 
#   7 | *
#   6 |           *
#   5 |     *
#   4 |              *
#   3 |        *
#   2 |
#   1 |   *
#      ----------------
"""
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