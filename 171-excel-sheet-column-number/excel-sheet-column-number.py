class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        """
        A -> 1

        """
        for i in range(len(columnTitle)-1, -1, -1):
            number += 26**(len(columnTitle)-i-1)*(ord(columnTitle[i])-64)
        return number

        