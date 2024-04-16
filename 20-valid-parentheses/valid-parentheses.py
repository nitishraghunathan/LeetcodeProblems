class Solution:
    def isValid(self, s: str) -> bool:
        map_dict = {')' : '(', '}': '{', ']':'['}
        stack = []
        for value in s:
            if value == '(' or value == '{' or value =='[':
                stack.append(value)
            else:
                if stack and stack[-1] == map_dict[value]:
                    stack.pop()
                else:
                    return False
        return not stack