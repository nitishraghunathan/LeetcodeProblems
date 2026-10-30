class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def recursion(combo:str, open:int, close:int):
            nonlocal result
            if close == 0 and open == 0:
                result.append(combo)
                return
            if open > 0:
                recursion(combo + '(', open-1, close)
            if open < close:
                recursion(combo + ')', open, close-1)
        recursion("", n, n)
        return result
            
            
        