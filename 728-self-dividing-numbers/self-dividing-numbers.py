class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def check_eligibility(num):
            original_num = num
            while num > 0:
                remainder = num%10
                if remainder == 0 or original_num%remainder!=0:
                    return False
                num = num //10
            return True
        result = []
        for i in range(left, right+1):
            if check_eligibility(i):
                result.append(i)
        return result

        