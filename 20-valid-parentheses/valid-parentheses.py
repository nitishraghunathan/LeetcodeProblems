class Solution:
    def isValid(self, s: str) -> bool:
        map_dict = { "}" : "{", ")":"(", "]" : "["}
        map_set = set()
        map_set.add("{")
        map_set.add("(")
        map_set.add("[")
        stack = []
        for index, value in enumerate(s):
            if value in map_set:
                stack.append(value)
            elif value in map_dict and len(stack) > 0 and  stack[-1] == map_dict[value]:
                stack.pop()
            else:
                return False
        return not stack

        