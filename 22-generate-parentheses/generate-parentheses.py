class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Have two counters for tracking the one for the open brackets and the other closing brackets
        keep appending open brackets as long as open count is less than close,
        backtrack adn send for other open close combinations
        append the closing bracket only if the open count is less than the close return the result
        finally when the size of the string is 2*n then append it to result
        """
        result = []
        def recursion(open:int, close:int, n:int, parenthesis: str):
            nonlocal result
            if len(parenthesis) == 2*n:
                result.append(parenthesis)
                return result
            if open > 0:
                parenthesis += "("
                result = recursion(open-1, close, n, parenthesis)
                parenthesis = parenthesis[:len(parenthesis)-1]
            if close > open:
                parenthesis += ")"
                result = recursion(open, close-1, n, parenthesis)
            return result
        return recursion(n,n,n,"")