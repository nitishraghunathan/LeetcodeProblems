class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        sum_total = ''
        counter = 0
        while columnNumber != 0:
            sum_total = chr(65 + (columnNumber-1)%26) +sum_total
            columnNumber = (columnNumber-1)//26
        return sum_total



        