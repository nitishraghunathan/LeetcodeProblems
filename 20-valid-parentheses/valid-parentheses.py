class Solution:
    def isValid(self, s: str) -> bool:
        """
        1. Define a dictionary with matching bracket types 
        2. Create a stack and all opening brackets 
        3. Once we confront a  closing bracket, popnthe elemtn from the stack and check if the bracket matches 
        4. If a match is not found return False
        5. Continue till the string is complete 
        6. Return if stack is empty to match rule 3 and 1
        """
        bracket_dict= {')' : '(', ']' :'[', '}' : '{'}
        bracket_stack = []
        for bracket in s:
            if bracket in bracket_dict:
                compare_char = bracket_stack.pop() if bracket_stack else None
                if compare_char != bracket_dict.get(bracket):
                    return False
            else:
                bracket_stack.append(bracket)
        return not bracket_stack
