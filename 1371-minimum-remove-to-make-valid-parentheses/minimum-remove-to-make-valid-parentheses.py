class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        add all brackets to the stack
        push the element to the stack i fpopped push the right stack
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
        push_stack = sorted(push_stack, key=lambda x:x[1])
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