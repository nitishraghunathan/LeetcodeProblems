class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        1. Add all the strings to the stack
        2. When there is an operator pop two stack elements and perfrom operations and append them back to the slack
        3. If there are no operators it is assumed to be addition
        """
        stack = []
        for index, value in enumerate(tokens):
            if value == '+':
                if len(stack) > 1:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a+b)
            elif value == '-':
                if len(stack) > 1:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)
            elif value == '*':
                if len(stack) > 1:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b*a)
            elif value == '/':
                if len(stack) > 1:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b/a))
            else:
                stack.append(int(value))
        return stack.pop()
