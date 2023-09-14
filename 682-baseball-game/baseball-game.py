class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
        1. Add all operands to the stack 
        2. Pop elements according the operator or capital character
        3. Perfrom special operations
        4. sum all elements in the stack
        """
        stack = []
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1]*2)
            else:
                stack.append(int(op))
        return sum(stack)