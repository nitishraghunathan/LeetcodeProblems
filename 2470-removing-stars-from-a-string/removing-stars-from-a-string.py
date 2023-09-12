class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for star in s:
            if star != '*':
                stack.append(star)
            else:
                if stack:
                    stack.pop()
        return "".join(stack)