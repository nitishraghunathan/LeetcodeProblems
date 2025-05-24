class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def convert_to_integer(num:str):
            new_num = 0
            for i in range(len(num)-1, -1, -1):
                new_num += pow(2, len(num)-1-i)*int(num[i])
            return new_num
        def convert_to_binary_str(num:int):
            binary_str = ''
            if num == 0:
                return '0'
            while num!=0:
                binary_str = str(num%2) + binary_str
                num = num//2
            return binary_str
        first_operator = convert_to_integer(a)
        second_operator = convert_to_integer(b)
        operator_sum = first_operator + second_operator
        final_binary_str = convert_to_binary_str(operator_sum)
        return final_binary_str




        