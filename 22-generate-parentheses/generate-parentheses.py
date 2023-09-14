class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        1. Generate complete parenthesis pairs
        2. The opening and closing braces should be matched
        3. Consider nesting cases
        4. perfrom recursion, backtrack and generate combinations
        """
        def generator(n:int, string:str, result: List[str], start:int, end:int)->List[str]:
            if len(string) == 2*n:
                result.append(string)
                return result
            if start > 0:
                string +='('
                result = generator(n, string, result, start-1, end)
                string = string[0:len(string)-1]
            if end > start:
                string += ')'
                result = generator(n,string, result, start, end-1)
            return result
        return generator(n, '', [], n, n)
        