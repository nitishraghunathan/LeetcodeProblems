class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_dict = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char not in map_dict:
                stack.append(char)
            else:
                if stack:
                    if stack[-1] != map_dict[char]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        return not stack