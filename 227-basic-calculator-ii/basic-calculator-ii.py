class Solution:
    def calculate(self, s: str) -> int:
        current_result, current_num, result = 0,0,0
        s += '+'
        sign = '+'
        for i in range(len(s)):
            current_char = s[i]
            if current_char.isdigit():
                current_num = current_num*10 +int(s[i])
            elif current_char in {'-', '+', '*', '/'}:
                if sign == '+':
                    current_result += current_num
                if sign == '-':
                    current_result -= current_num
                if sign == '*':
                    current_result *= current_num
                if sign == '/':
                    current_result = int(current_result/current_num)
                if current_char in {'+','-'}:
                    result += current_result
                    current_result = 0
                sign = current_char
                current_num=0
        return result