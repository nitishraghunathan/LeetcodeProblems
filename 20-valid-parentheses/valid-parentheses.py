class Solution:
    def isValid(self, s: str) -> bool:
        map_dict = {'}' : '{', ']' : '[', ')':'('}
        stack = []
        for brackets in s:
            if brackets not in map_dict:
                stack.append(brackets)
            else:
                if not stack or map_dict[brackets] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack
