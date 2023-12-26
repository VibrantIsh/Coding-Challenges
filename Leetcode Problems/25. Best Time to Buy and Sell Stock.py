# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0
        
        x, y = 0, prices[0]
        
        for i in prices[1:]:
            y = min(y, i)
            x = max(x, i - y)
                
        return x
