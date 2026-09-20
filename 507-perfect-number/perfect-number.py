import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # Perfect numbers must be positive and strictly greater than 1
        if num <= 1:
            return False
        
        # Start sum with 1, as 1 is a proper divisor for all numbers > 1
        total_sum = 1
        
        # Iterate up to sqrt(num)
        for i in range(2, int(math.isqrt(num)) + 1):
            if num % i == 0:
                total_sum += i
                # Add the matching paired divisor if it's not the square root itself
                if i * i != num:
                    total_sum += num // i
            
            # Early exit optimization if sum already exceeds num
            if total_sum > num:
                return False
                
        return total_sum == num