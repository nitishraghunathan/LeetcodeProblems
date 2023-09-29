class Solution:
    def decodeString(self, s: str) -> str:
        """
        1. Add all the strings to a stack one by one till we reach a closing brace
        2. Pop all elements once we reach the closing brace till we have opening brace
        3. Pop the opening brace
        4. Pop the strings as long as they are digits
        5. convert the finalpopped numbers into an int and mulitply with the first popped string and then append it back to the stack
        7. Finally join all the strings in the stack
        """
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                sub_str = ''
                while stack[-1] != '[':
                    sub_str = stack.pop() +sub_str
                stack.pop()
                number= ''
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                stack.append(int(number)*sub_str)
        return ''.join(stack)