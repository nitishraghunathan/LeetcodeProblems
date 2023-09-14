class Solution:
    def removeStars(self, s: str) -> str:
        """
        1. Add all characters to the stack 
        2. Whenever there is a star pop the character from stack 
        3. return the string after popping the elements

        """
        stack = []
        for star in s:
            if star != '*':
                stack.append(star)
            else:
                if stack:
                    stack.pop()
        return "".join(stack)
        