class Solution:
    def removeStars(self, s: str) -> str:
        """
        1. Add all the characters to the stack 
        2. Whenever there is a star, pop the character from the stack
        3. Return the string after iterating over all star characters
        """
        stack =[]
        for star in s:
            if star!='*':
                stack.append(star)
            else:
                if stack:
                    stack.pop()
        return "".join(stack)
        