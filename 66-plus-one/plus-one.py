class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return 0
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if carry == 0:
                return digits
            else:
                total_sum = (carry+digits[i])%10
                carry = (carry+digits[i])//10
                digits[i] = total_sum
        if carry:
            digits.insert(0,carry)
        return digits
        