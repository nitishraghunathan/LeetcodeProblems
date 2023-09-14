class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        1. Add all the strings to the stack
        2. When there is an operator pop two stack elements and perfrom operations and append them back to the slack
        3. If there are no operators it is assumed to be addition
        """
        polish_stack = []

        for expression in tokens:
            if expression == '+' or expression == '-' or expression == '*' or expression == '/':
                polish_sum = 0
                first_num = polish_stack.pop()
                second_num = polish_stack.pop()
                if expression == '+':
                    polish_sum = second_num + first_num
                if expression == '-':
                    polish_sum = second_num - first_num
                if expression == '*':
                    polish_sum = second_num * first_num
                if expression == '/':
                    polish_sum = int(second_num/first_num)
                polish_stack.append(polish_sum)
            else:
                polish_stack.append(int(expression))
        return int(polish_stack.pop())