class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for index, value in enumerate(prices):
            min_price = min(value, min_price)
            max_profit = max(max_profit, value - min_price)
        return max_profit