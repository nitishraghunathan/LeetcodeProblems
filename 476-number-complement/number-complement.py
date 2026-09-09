class Solution:
    def findComplement(self, num: int) -> int:
        result = ""
        while num > 0:
            if num%2 == 1:
                result = str(1^1) + result
            else:
                result = str(0^1) + result
            num = num//2
        complement = ""
        carry = 1
        for i in range(len(result)-1, -1, -1):
            sum_val = carry + int(result[i])
            complement = str(sum_val%2) + complement
            carry = sum_val//2
        if carry > 0:
            complement  = str(carry) + complement 
        total_num = 0
        for i in range(len(complement)-1, -1, -1):
            total_num += 2**(len(result)-1-i)*int(complement[i])
        return total_num-1

