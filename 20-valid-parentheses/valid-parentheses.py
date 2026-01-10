class Solution:
    def isValid(self, s: str) -> bool:
        map_dict = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for index, value in enumerate(s):
            if value in map_dict and stack:
                diff = stack.pop()
                if map_dict[value] != diff:
                    return False
            else:
                stack.append(value)
        return not stack


        