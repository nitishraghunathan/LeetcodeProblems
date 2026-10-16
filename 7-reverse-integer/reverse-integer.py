class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Handle sign and make x positive
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_int = 0
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow before multiplying by 10
            if reversed_int > (INT_MAX - digit) // 10:
                return 0
                
            reversed_int = reversed_int * 10 + digit
            
        return sign * reversed_int