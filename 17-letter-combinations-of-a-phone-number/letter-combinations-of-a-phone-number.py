class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        map_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        def combinations(digits, index, string):
            nonlocal result
            if index == len(digits):
                result.append(string)
                return result
            for i in map_dict[digits[index]]:
                result = combinations(digits, index+1, string+i)
            return result
        return combinations(digits, 0, "")