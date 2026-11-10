class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        result = 0
        sign = 1  # 1 means positive, -1 means negative
        
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '+':
                result += sign * current_number
                current_number = 0
                sign = 1
            elif char == '-':
                result += sign * current_number
                current_number = 0
                sign = -1
            elif char == '(':
                # Push the current result and sign onto the stack
                stack.append(result)
                stack.append(sign)
                # Reset for the new sub-expression inside parentheses
                result = 0
                sign = 1
            elif char == ')':
                result += sign * current_number
                current_number = 0
                # Multiply by the sign before the parenthesis
                result *= stack.pop()
                # Add the result calculated before the parenthesis opened
                result += stack.pop()
                
        # Add any remaining number
        result += sign * current_number
        return result