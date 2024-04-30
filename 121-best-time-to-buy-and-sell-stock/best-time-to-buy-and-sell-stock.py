class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = float('-inf')
        min_price = float('inf')
        for index,value in enumerate(prices):
            min_price = min(value, min_price)
            profit = max(profit, value - min_price)
        return profit