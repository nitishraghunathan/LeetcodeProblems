class Solution:
    def countBits(self, n: int) -> List[int]:
        def one_bit_counter(n):
            counter = 0
            while n > 0:
                if n%2 == 1:
                    counter+=1
                n = n//2
            return counter
        return [one_bit_counter(i) for i in range(n+1)]