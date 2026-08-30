class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        prime_factors = [2, 3, 5]
        for factors in prime_factors:
            while n%factors==0:
                n //= factors
        return n==1