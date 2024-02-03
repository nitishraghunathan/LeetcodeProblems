class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = 0
        for words in s:
            if words == '(':
                stack.append(words)
                max_depth = max(len(stack), max_depth)
            if words == ')':
                stack.pop()
        return max_depth