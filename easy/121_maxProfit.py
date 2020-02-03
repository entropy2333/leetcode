class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        buy = prices[0]
        profit = 0
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price-buy)
        return profit
    