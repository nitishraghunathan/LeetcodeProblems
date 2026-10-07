class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join([value.lower() for index, value in enumerate(s)])

        