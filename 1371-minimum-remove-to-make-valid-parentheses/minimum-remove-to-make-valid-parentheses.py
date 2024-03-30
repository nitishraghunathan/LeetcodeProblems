class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        add all open brackets to reject stack if close bracket and reject stack's last element is open
        we pop the elements and add them push_stack.
        else we add the close bracket to reject stack 
        we add to push stack and then add indexes to a set and create a new_string add brackets if indexes are in a set
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