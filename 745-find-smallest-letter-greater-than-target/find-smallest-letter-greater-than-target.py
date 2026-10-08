class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for value in letters:
            if value > target:
                return value
        return letters[0]
        