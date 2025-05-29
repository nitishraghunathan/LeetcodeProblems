class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in set(["+", "-", "*", "/"]):
                if len(stack) > 1:
                    a = stack.pop()
                    b = stack.pop()
                    sum_value = 0
                    if token == '+':
                        sum_value = int(a) + int(b)
                    elif token == '-':
                        sum_value = int(b) - int(a)
                    elif token == '*':
                        sum_value = int(a) * int(b)
                    else:
                        sum_value = int(int(b)/int(a))
                    stack.append(str(sum_value))
                else:
                    return -1
            else:
                stack.append(token)
            
        return int(stack.pop()) if stack else -1

        