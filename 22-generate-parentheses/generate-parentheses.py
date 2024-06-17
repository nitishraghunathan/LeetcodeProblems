class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        1. Generate complete parenthesis pairs
        2. The opening and closing braces should be matched
        3. Consider nesting cases
        4. perfrom recursion, backtrack and generate combinations
        """
        result = []
        def generate(open, close, string):
            nonlocal result, n
            if len(string) == 2*n:
                result.append(string)
                return result
            if open > 0:
                string += '('
                result = generate(open-1, close, string)
                string = string[:len(string)-1]
            if close  > open:
                string += ')'
                result = generate(open, close-1, string)
            return result
        return generate(n, n, '')
        