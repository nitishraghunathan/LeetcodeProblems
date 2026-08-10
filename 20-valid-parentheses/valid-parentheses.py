class Solution:
    def isValid(self, s: str) -> bool:
        map_dict = {")" : "(", "]" : "[", "}" : "{"}
        stack = []
        for index, value in enumerate(s):
            if value not in map_dict:
                stack.append(value)
            else:
                if stack:
                    val = stack.pop()
                    if val != map_dict[value]:
                        return False
                else:
                    return False
        return not stack

        