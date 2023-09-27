class StockSpanner:
    """
    1. Return consecutive days for which stock is less than or equal to todays stock
    2. Keep track of the dasy as well as the stock price
    3. Initialize  asstack and pop elements if less than the curreent day's value
    4. Reurn the sum of the popped elements consective days which gives current  stack values' span
    """

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        stack = self.stack
        result = 1
        while stack and stack[-1][0] <= price:
            result += stack.pop()[1]
        stack.append([price, result])
        return result
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)