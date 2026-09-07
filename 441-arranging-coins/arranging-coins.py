class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 2:
            return n
        for i in range (1, n+1):
            if n < i:
                return i-1
            n = n-i
        return n