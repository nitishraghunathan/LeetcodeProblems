class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        max_distance = 0
        stack.append(["", -1])
        for index,value in enumerate(s):
            if value == '(':
                stack.append([value, index])
            else:
                if stack and stack[-1][0] == "(":
                    stack.pop()
                    max_distance = max(max_distance, index-stack[-1][1])
                else:
                    stack.append([value, index])
        return max_distance