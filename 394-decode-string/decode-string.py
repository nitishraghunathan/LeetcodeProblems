class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                sub_str = ''
                while stack[-1] != '[':
                    sub_str = stack.pop() + sub_str
                stack.pop()
                number = ''
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                stack.append(sub_str*int(number))
        return "".join(stack)
        
