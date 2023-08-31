class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == '+':
                addend_one = stack.pop() if stack else 0
                addend_two = stack.pop() if stack else 0
                stack.append(addend_two)
                stack.append(addend_one)
                stack.append(addend_one+addend_two)
            elif operation == 'D':
                previous_double = stack.pop() if stack else 0 
                stack.append(previous_double)
                stack.append(previous_double*2)
            elif operation == 'C':
                stack.pop()
            else:
                stack.append(int(operation))
        sum_stack = 0
        while stack:
            sum_stack += stack.pop()
        return sum_stack