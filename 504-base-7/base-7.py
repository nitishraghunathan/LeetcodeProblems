class Solution:
    def convertToBase7(self, num: int) -> str:
        new_str = ""
        flag = False
        if num == 0:
            return "0"
        if num < 0 :
            num  = -num
            flag = True
        while num > 0:
            new_str =str(num%7) +new_str
            num = num//7
        return new_str if not flag else "-" + new_str
            
        