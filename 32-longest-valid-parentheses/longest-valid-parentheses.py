class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        1. Initialize a stack and keep track of the index of the brackets
        2. if open then just push it along with index 
        3. if closed check if last element is open or push it in the stack with index to for counting new subsrtring

        """
        stack = []
        max_value = 0
        stack.append(['', -1])
        for index,value in enumerate(s):
            if value == '(':
                stack.append([value,index])
            else:
                if stack and stack[-1][0] == '(':
                    sum_value = 0
                    stack.pop()
                    sum_value= index -stack[-1][1]
                    max_value = max(max_value, sum_value)
                else:
                    stack.append([value, index])
        return max_value