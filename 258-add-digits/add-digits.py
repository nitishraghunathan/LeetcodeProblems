class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            sum_num = 0
            while num != 0:
                sum_num += num%10
                num = num//10
            if sum_num//10 ==0:
                return sum_num
            num = sum_num


        