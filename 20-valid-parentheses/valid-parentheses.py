class Solution:
    def isValid(self, s: str) -> bool:
        """
        every bracket would have a closure 
        (', ')', '{', '}', '[' and ']'
        if in the event 
        we have 
        (].Not valid 
        if it is empty - valid 
        if there is more closing  parenthesis or more empty parenthesis than equal it is not true
        put all elements in the stack  if it is an opening bracket 
        if it is a closing bracket pop it out from the stack and check the bracket matches 
        """
        bracket_stack = []
        bracket_dict = {')' : '(', '}' : '{', ']' : '['}
        for bracket in s:
            if bracket in bracket_dict:
                compare_char = bracket_stack.pop() if bracket_stack else None
                if compare_char != bracket_dict.get(bracket):
                    return False
            else:
                bracket_stack.append(bracket)
        return not bracket_stack