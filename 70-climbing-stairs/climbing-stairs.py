class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        a = 1
        b = 1
        for i in range(2, n+1):
            c = a+b
            a, b = b, c
        return b