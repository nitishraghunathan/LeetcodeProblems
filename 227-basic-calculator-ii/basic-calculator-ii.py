class Solution:
    def calculate(self, s: str) -> int:
        result, current_result, current_num = 0,0,0
        s += '+'
        sign ='+'
        for i in range(len(s)):
            current_character = s[i]
            if current_character.isdigit():
                current_num = current_num*10 + int(s[i])
            if current_character in {'+', '-', '/', '*'}:
                if sign == '+':
                    current_result += current_num
                elif sign == '-':
                    current_result -= current_num
                elif sign == '*':
                    current_result *= current_num
                elif sign == '/':
                    current_result = int(current_result/current_num)
                if current_character in {'+','-'}:
                    result += current_result
                    current_result = 0
                sign = current_character
                current_num = 0
        return result