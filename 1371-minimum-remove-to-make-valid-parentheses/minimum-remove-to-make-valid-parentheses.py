class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        add all open brackets to reject stack if close bracket and reject stack's last element is open
        we pop the elements and add them push_stack.
        else we add the close brakc to reject stack 
        we push stack by index and create a new_string
        """
        push_stack= []
        reject_stack = []
        for index, c in enumerate(s):
            if c == '(':
                reject_stack.append(['(', index])
            elif c == ')':
                if reject_stack and reject_stack[-1][0] == '(':
                    push_stack.append(reject_stack.pop())
                    push_stack.append([')', index])
                else:
                    reject_stack.append([')', index])
        index_set = set()
        for numbers in push_stack:
            index_set.add(numbers[1])
        new_string = ''
        for index, c in enumerate(s):
            if c== '(' or c==')':
                if index in index_set:
                    new_string +=c
            else:
                new_string +=c
        return new_string


        return ''.join(result)