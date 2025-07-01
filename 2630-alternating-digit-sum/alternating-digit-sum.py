class Solution:
    def alternateDigitSum(self, n: int) -> int:
        number = str(n)
        sign = 1
        sum_number = 0
        for i in number:
            sum_number += int(i)*sign
            sign = -sign
        return sum_number 

        