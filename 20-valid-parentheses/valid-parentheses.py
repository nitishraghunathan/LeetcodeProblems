class Solution:
    def isValid(self, s: str) -> bool:
        map_dict = {")":"(", "}": "{", "]":"["}
        stack = []
        for index, value in enumerate(s):
            if value in map_dict:
                if not stack or stack.pop() != map_dict[value]:
                    return False
            else:
                stack.append(value)
        return len(stack) == 0

            
        