class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for string in s:
            if string != ']':
                stack.append(string)
            else:
                substring = ''
                while stack and stack[-1]!='[':
                    substring = stack.pop() + substring
                stack.pop()
                number = ''
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                stack.append(int(number)*substring)
        substring =''
        while stack:
            substring = stack.pop() + substring
        return substring