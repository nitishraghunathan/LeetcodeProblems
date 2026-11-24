class Solution:
    def reverseBits(self, n: int) -> int:
        def convert_to_binary_string(n:int):
            string = ""
            while n > 0:
                string = str(n%2) + string
                n = n//2
            if len(string) < 32:
                string = "0"*(32-len(string)) +string
            return string
        def convert_to_integer(string:str):
            string = string[::-1]
            integer = 0
            for i in range(32):
                integer+= (2**(31-i))*int(string[i])
            return integer
        return convert_to_integer(convert_to_binary_string(n))

