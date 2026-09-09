class Solution:
    def findComplement(self, num: int) -> int:
        # Step 1: Extract digits and invert them using XOR (One's Complement)
        result = ""
        while num > 0:
            if num % 2 == 1:
                result = str(1 ^ 1) + result  # Turns 1 into 0
            else:
                result = str(0 ^ 1) + result  # Turns 0 into 1
            num = num // 2
            
        # Step 2: Convert the flipped binary string directly back to a decimal integer
        total_num = 0
        length = len(result)
        for i in range(length - 1, -1, -1):
            total_num += 2 ** (length - 1 - i) * int(result[i])
            
        return total_num
