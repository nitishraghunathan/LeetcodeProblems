class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                if len(stack) > 1:
                    second = stack.pop()
                    first = stack.pop()
                    total_sum = 0
                if token == '+':
                    total_sum  = first + second 
                elif token == '-':
                    total_sum = first-second
                elif token == '*':
                    total_sum = first*second
                else:
                    total_sum = int(first/second) if second !=0 else 0
                stack.append(total_sum)
        return stack.pop()

        