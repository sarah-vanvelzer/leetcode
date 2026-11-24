# Pattern: track maximum profit SO FAR
# Time: O(n)
# Space: O(1)
# Revisit: no

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Inputs: array of prices
        # Outputs: maximum difference between two numbers
        #   where ending price is at later index than starting
        # Cannot sell on day 1

        min_price = prices[0]
        max_diff = 0

        # for loops with range stop at "stop - 1"
        for i in range(1, len(prices), 1):
            if prices[i] - min_price > max_diff:
                max_diff = prices[i] - min_price
            if prices[i] < min_price:
                min_price = prices[i]
        
        return max_diff