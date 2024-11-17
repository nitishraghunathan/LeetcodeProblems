class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n:
            counter += 1 if n%2==1 else 0
            n = n//2
        return counter