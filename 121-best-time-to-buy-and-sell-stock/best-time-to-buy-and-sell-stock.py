class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = float('-inf')
        for index, value in enumerate(prices):
            min_price = min(min_price, value)
            profit = max(profit, value - min_price)
        return profit
        