class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        temp = 0
        for bracket in brackets:
            if income == 0:
                return tax
            elif bracket[0] - temp <= income:
                income -= (bracket[0] - temp)
                tax += ((bracket[0] - temp)*bracket[1])/100
                temp = bracket[0]
            else:
                tax += (income*bracket[1])/100
                income = 0
        return tax